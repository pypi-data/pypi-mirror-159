from __future__ import absolute_import

import imghdr
import io
import os
import struct
from typing import List, Optional, Tuple

from slideflow import errors
from slideflow.util import example_pb2, extract_feature_dict, log


def detect_tfrecord_format(tfr: str) -> Tuple[Optional[List[str]],
                                              Optional[str]]:
    '''Detects tfrecord format.

    Args:
        tfr (str): Path to tfrecord.

    Returns:
        list(str): List of detected features.
        str: Image file type (png/jpeg)
    '''
    typename_mapping = {
        "byte": "bytes_list",
        "float": "float_list",
        "int": "int64_list"
    }
    feature_description = {
        'image_raw': 'byte',
        'slide': 'byte',
        'loc_x': 'int',
        'loc_y': 'int'
    }

    def process(record, description):
        example = example_pb2.Example()
        example.ParseFromString(record)
        return extract_feature_dict(
            example.features,
            description,
            typename_mapping)

    length_bytes = bytearray(8)
    crc_bytes = bytearray(4)
    datum_bytes = bytearray(1024 * 1024)
    file = io.open(tfr, 'rb')
    if not os.path.getsize(tfr):
        log.debug(f"Unable to detect format for {tfr}; file empty.")
        return None, None
    file.tell()
    if file.readinto(length_bytes) != 8:
        raise RuntimeError("Failed to read the record size.")
    if file.readinto(crc_bytes) != 4:
        raise RuntimeError("Failed to read the start token.")
    length, = struct.unpack("<Q", length_bytes)
    if length > len(datum_bytes):
        try:
            datum_bytes = datum_bytes.zfill(int(length * 1.5))
        except OverflowError:
            raise OverflowError('Error reading tfrecords; please try '
                                'regenerating index files')
    datum_bytes_view = memoryview(datum_bytes)[:length]
    if file.readinto(datum_bytes_view) != length:
        raise RuntimeError("Failed to read the record.")
    if file.readinto(crc_bytes) != 4:
        raise RuntimeError("Failed to read the end token.")
    try:
        record = process(datum_bytes_view, description=feature_description)
    except KeyError:
        feature_description = {
            k: v for k, v in feature_description.items()
            if k in ('slide', 'image_raw')
        }
        try:
            record = process(datum_bytes_view, description=feature_description)
        except KeyError:
            raise errors.TFRecordsError(
                f'Unable to detect TFRecord format: {tfr}'
            )
    img = bytes(record['image_raw'])
    img_type = imghdr.what('', img)
    return list(feature_description.keys()), img_type
