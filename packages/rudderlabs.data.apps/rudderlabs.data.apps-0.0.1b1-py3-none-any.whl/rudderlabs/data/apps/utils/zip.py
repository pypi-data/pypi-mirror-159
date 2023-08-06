#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compress and decompress a directory."""

import os
import tempfile
import zipfile

from ..constants import EXCLUDE_FOLDERS
from ..log import get_logger

TEMP_DIR = tempfile.gettempdir()
logger = get_logger(__name__)


def zip_directory(dir_path: str) -> str:
    """Zip the given directory

    Args:
        dir_path: Directory path

    Returns:
        str: Path to the zipped directory
    """
    logger.info("Zipping directory")
    dir_name = os.path.basename(dir_path)

    zip_path = os.path.join(TEMP_DIR, dir_name + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(dir_path):

            # Exclude folders
            for dirname in dirs:
                if (
                    dirname in EXCLUDE_FOLDERS
                    or dirname.startswith(".")
                    or dirname.startswith("__")
                ):
                    dirs.remove(dirname)

            for file in files:
                if file.startswith(".") or file.startswith("__"):
                    continue
                abs_file_path = os.path.join(root, file)
                zip_file.write(
                    abs_file_path, abs_file_path.replace(dir_path, "")
                )
    return zip_path


def unzip_directory(zip_path: str, out_dir_path: str) -> None:
    """Unzip the directory

    Args:
        zip_path: Path to the zipped directory
        dir_path: Output directory path

    Returns:
        None: None
    """
    logger.info("Unzipping directory")
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        zip_file.extractall(out_dir_path)
