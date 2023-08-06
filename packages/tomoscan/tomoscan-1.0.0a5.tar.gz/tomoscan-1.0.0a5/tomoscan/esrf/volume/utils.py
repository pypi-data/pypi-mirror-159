# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2022 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/
"""utils function for esrf volumes"""


__authors__ = [
    "H. Payno",
]
__license__ = "MIT"
__date__ = "11/07/2022"


import os
import h5py
from tomoscan.esrf.volume.edfvolume import EDFVolume
from tomoscan.esrf.volume.hdf5volume import HDF5Volume
from tomoscan.esrf.volume.tiffvolume import MultiTIFFVolume, TIFFVolume
from tomoscan.esrf.volume.jp2kvolume import JP2KVolume
from tomoscan.io import HDF5File
import logging

_logger = logging.getLogger(__name__)


def guess_hdf5_volume_data_paths(file_path, data_path="/", depth=3) -> tuple:
    """
    browse hdf5 file 'file_path' from 'data_path' on 'depth' level and check for possible defined volumes.

    :param str file_path: file path to the hdf5 file to browse
    :param str data_path: path in the file to start research
    :param int depth: on which layer we should apply research
    :return: tuple of data_path that could fit a volume
    :rtype: tuple
    """
    if not h5py.is_hdf5(file_path):
        raise ValueError(f"{file_path} is not a hdf5 file path")
    with HDF5File(filename=file_path, mode="r") as h5f:
        group = h5f[data_path]
        if isinstance(group, h5py.Group):
            if HDF5Volume.DATA_DATASET_NAME in group:
                return (data_path,)
            elif depth > 0:
                res = []
                for key in group.keys():
                    res.extend(
                        guess_hdf5_volume_data_paths(
                            file_path=file_path,
                            data_path="/".join((data_path, key)).replace("//", "/"),
                            depth=depth - 1,
                        )
                    )
                return tuple(res)

        return tuple()


def guess_volumes(path) -> tuple:
    """
    from a file path or a folder path try to guess volume(s)

    :param str path: file or folder path
    :return: tuple of volume
    :rtype: tuple
    """
    if not os.path.exists(path):
        raise OSError("path doesn't exists")

    if os.path.isfile(path):
        if h5py.is_hdf5(path):
            res = []
            for data_path in guess_hdf5_volume_data_paths(path):
                assert isinstance(data_path, str)
                res.append(
                    HDF5Volume(
                        file_path=path,
                        data_path=data_path,
                    )
                )
            return tuple(res)
        elif path.lower().endswith((".tif", ".tiff")):
            return (MultiTIFFVolume(file_path=path),)
    elif os.path.isdir(path):
        most_common_extension = _get_most_common_extension(path)
        if most_common_extension is None:
            return tuple()

        basename = _guess_volume_basename(path, extension=most_common_extension)
        if most_common_extension in ("tiff", "tif"):
            return (
                TIFFVolume(
                    folder=path,
                    volume_basename=basename,
                    data_extension=most_common_extension,
                ),
            )
        elif most_common_extension in ("jp2", "jp2k"):
            return (
                JP2KVolume(
                    folder=path,
                    volume_basename=basename,
                    data_extension=most_common_extension,
                ),
            )
        elif most_common_extension == "edf":
            return (
                EDFVolume(
                    folder=path,
                    volume_basename=basename,
                    data_extension=most_common_extension,
                ),
            )
        else:
            _logger.warning(
                f"most common extension is {most_common_extension}. Unable to create a volume from it"
            )
            return tuple()
    else:
        raise NotImplementedError("guess_volumes only handle file and folder...")


def _get_most_common_extension(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError(f"a folder path is expected. {folder_path} isn't")

    extensions = {}
    for file_path in os.listdir(folder_path):
        _, ext = os.path.splitext(file_path)
        ext = ext.lower().lstrip(".")
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1

    # filter not handled extensions
    def is_valid_extension(extension):
        return extension in ("edf", "tif", "tiff", "jp2", "jp2k")

    extensions = {
        key: value for (key, value) in extensions.items() if is_valid_extension(key)
    }

    if len(extensions) == 0:
        _logger.warning(f"no valid extensions found in {folder_path}")
    else:
        sort_extensions = sorted(extensions.items(), key=lambda x: x[1], reverse=True)
        return sort_extensions[0][0]


def _guess_volume_basename(folder_path, extension):
    # list all the files matching the file and guessing the file parttern
    files_to_check = []
    possible_basenames = {}
    for file_path in os.listdir(folder_path):
        if file_path.lower().endswith(extension):
            files_to_check.append(os.path.splitext(file_path)[0])
            # the expected way to save those files is basename_XXXX with XXXX is the index over 4 char
            basename = "_".join(file_path.split("_")[:-1])
            if basename in possible_basenames:
                possible_basenames[basename] += 1
            else:
                possible_basenames[basename] = 1

    if len(possible_basenames) == 0:
        _logger.warning(f"no valid basename found in {folder_path}")
    else:
        sort_basenames = sorted(
            possible_basenames.items(), key=lambda x: x[1], reverse=True
        )
        if len(sort_basenames) > 1:
            _logger.warning(
                f"more than one basename found. Take the most probable one ({sort_basenames[0][0]})"
            )
        return sort_basenames[0][0]
