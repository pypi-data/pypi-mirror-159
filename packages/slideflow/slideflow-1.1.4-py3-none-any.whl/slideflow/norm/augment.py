"""
From https://github.com/wanghao14/Stain_Normalization
Stain normalization based on the method of:

M. Macenko et al., ‘A method for normalizing histology slides for quantitative analysis’,
in 2009 IEEE International Symposium on Biomedical Imaging: From Nano to Macro, 2009, pp. 1107–1110.

Uses the spams package:

http://spams-devel.gforge.inria.fr/index.html

Use with python via e.g https://anaconda.org/conda-forge/python-spams
"""

from __future__ import division

import numpy as np
import cv2 as cv
import slideflow.norm.utils as ut


class Normalizer(ut.BaseNormalizer):
    """
    A stain normalization object
    """

    def __init__(self):
        return

    def fit(self, target: np.ndarray) -> None:
        return

    def transform(self, I: np.ndarray) -> np.ndarray:

        hsv = cv.cvtColor(I, cv.COLOR_RGB2HSV)
        hsv[:, :, 2] = cv.equalizeHist(hsv[:, :, 2])
        hsv[:, :, 1] = cv.equalizeHist(hsv[:, :, 1])
        hsv = np.array(hsv, dtype=np.float64)
        hm = np.random.uniform(0.8, 1.2)
        ha = np.random.uniform(-0.2, 0.2)
        sm = np.random.uniform(0.8, 1.2)
        sa = np.random.uniform(-0.2, 0.2)
        vm = np.random.uniform(0.8, 1.2)
        va = np.random.uniform(-0.2, 0.2)
        hsv[:, :, 0] *= hm
        hsv[:, :, 1] *= sm
        hsv[:, :, 2] *= vm
        hsv[:, :, 0] += ha
        hsv[:, :, 1] += sa
        hsv[:, :, 2] += va
        hsv[hsv > 255] = 255
        hsv[hsv < 0] = 0
        hsv = np.array(hsv, dtype=np.uint8)
        img = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
        return img

