"""PyTorch model utility functions."""

import torch
import types
from typing import Iterable, Generator, Tuple, Dict, List, Union


def cycle(iterable: Iterable) -> Generator:
    while True:
        for i in iterable:
            yield i


def print_module_summary(
    module: torch.nn.Module,
    inputs: List[torch.Tensor],
    max_nesting: int = 3,
    skip_redundant: bool = True
) -> str:
    """Prints and returns summary of a torch module.

    Args:
        module (torch.nn.Module): PyTorch module.
        inputs (torch.Tensor): Input tensors, for calculating layer sizes.
        max_nesting (int, optional): Module depth. Defaults to 3.
        skip_redundant (bool, optional): Skip redundant entries.
            Defaults to True.

    Returns:
        str: Summary of the module.
    """
    assert isinstance(module, torch.nn.Module)
    assert not isinstance(module, torch.jit.ScriptModule)
    assert isinstance(inputs, (tuple, list))

    # Register hooks.
    entries = []
    nesting = [0]

    def pre_hook(_mod, _inputs):
        nesting[0] += 1

    def post_hook(mod, _inputs, outputs):
        nesting[0] -= 1
        if nesting[0] <= max_nesting:
            outputs = list(outputs) if isinstance(outputs, (tuple, list)) else [outputs]
            outputs = [t for t in outputs if isinstance(t, torch.Tensor)]
            entries.append(types.SimpleNamespace(mod=mod, outputs=outputs))

    hooks = [mod.register_forward_pre_hook(pre_hook) for mod in module.modules()]
    hooks += [mod.register_forward_hook(post_hook) for mod in module.modules()]

    # Run module.
    module(*inputs)
    for hook in hooks:
        hook.remove()

    # Identify unique outputs, parameters, and buffers.
    tensors_seen = set()
    for e in entries:
        e.unique_params = [t for t in e.mod.parameters() if id(t) not in tensors_seen]
        e.unique_buffers = [t for t in e.mod.buffers() if id(t) not in tensors_seen]
        e.unique_outputs = [t for t in e.outputs if id(t) not in tensors_seen]
        tensors_seen |= {id(t) for t in e.unique_params + e.unique_buffers + e.unique_outputs}

    # Filter out redundant entries.
    if skip_redundant:
        entries = [e for e in entries if len(e.unique_params) or len(e.unique_buffers) or len(e.unique_outputs)]

    # Construct table.
    rows = [[type(module).__name__, 'Parameters', 'Buffers', 'Output shape', 'Datatype']]
    rows += [['---'] * len(rows[0])]
    param_total = 0
    buffer_total = 0
    submodule_names = {mod: name for name, mod in module.named_modules()}
    for e in entries:
        name = '<top-level>' if e.mod is module else submodule_names[e.mod]
        param_size = sum(t.numel() for t in e.unique_params)
        buffer_size = sum(t.numel() for t in e.unique_buffers)
        output_shapes = [str(list(e.outputs[0].shape)) for t in e.outputs]
        output_dtypes = [str(t.dtype).split('.')[-1] for t in e.outputs]
        rows += [[
            name + (':0' if len(e.outputs) >= 2 else ''),
            str(param_size) if param_size else '-',
            str(buffer_size) if buffer_size else '-',
            (output_shapes + ['-'])[0],
            (output_dtypes + ['-'])[0],
        ]]
        for idx in range(1, len(e.outputs)):
            rows += [[name + f':{idx}', '-', '-', output_shapes[idx], output_dtypes[idx]]]
        param_total += param_size
        buffer_total += buffer_size
    rows += [['---'] * len(rows[0])]
    rows += [['Total', str(param_total), str(buffer_total), '-', '-']]

    # Print table.
    widths = [max(len(cell) for cell in column) for column in zip(*rows)]
    summary_rows = []
    print()
    for row in rows:
        str_row = '  '.join(cell + ' ' * (width - len(cell)) for cell, width in zip(row, widths))
        summary_rows += [str_row]
        print(str_row)
    print()
    return '\n'.join(summary_rows)


def enable_dropout(m: torch.nn.Module) -> None:
    for module in m.modules():
        if module.__class__.__name__ == 'LinearBlock':
            for submodule in module.modules():
                if submodule.__class__.__name__.startswith('Dropout'):
                    submodule.train()


def get_uq_predictions(
    img: Union[torch.Tensor, Tuple[torch.Tensor, ...]],
    model: torch.nn.Module,
    num_outcomes: int,
    uq_n: int = 30
) -> Tuple[Union[torch.Tensor, List[torch.Tensor]],
           Union[torch.Tensor, List[torch.Tensor]],
           int]:
    """Performs UQ inference (mean and stdev/uncertainty), calculated
    using a set number of forward passes.

    Args:
        img (torch.Tensor): Batch of input images.
        model (torch.nn.Module): Model to use for inference.
        num_outcomes (int): Number of expected outcomes.
        uq_n (int, optional): Number of forward passes. Defaults to 30.

    Returns:
        torch.Tensor: Mean of forward passes.
        torch.Tensor: Standard deviation of forward passes.
        int: Number of detected outcomes.
    """
    enable_dropout(model)
    if not num_outcomes:
        yp_drop = {}  # type: Dict[int, List]
    else:
        yp_drop = {n: [] for n in range(num_outcomes)}
    for _ in range(uq_n):
        yp = model(*img)
        if not num_outcomes:
            num_outcomes = 1 if not isinstance(yp, (list, tuple)) else len(yp)
            yp_drop = {n: [] for n in range(num_outcomes)}
        if num_outcomes > 1:
            for o in range(num_outcomes):
                yp_drop[o] += [yp[o]]
        else:
            yp_drop[0] += [yp]
    if num_outcomes > 1:
        stacked = [torch.stack(yp_drop[n], dim=0) for n in range(num_outcomes)]
        yp_mean = [torch.mean(stacked[n], dim=0) for n in range(num_outcomes)]
        yp_std = [torch.std(stacked[n], dim=0) for n in range(num_outcomes)]
    else:
        stacked = torch.stack(yp_drop[0], dim=0)  # type: ignore
        yp_mean = torch.mean(stacked, dim=0)  # type: ignore
        yp_std = torch.std(stacked, dim=0)  # type: ignore
    return yp_mean, yp_std, num_outcomes
