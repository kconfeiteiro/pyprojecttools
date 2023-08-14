import glob
import os
from typing import (
    List,
    Tuple,
)


""" Sorting, deleting, copying files, and dealing with directories """


def delete_filetype(folder: str = ..., *filetypes: str) -> None:
    """Deletes files of specific type

    Args:
        folder (str, optional): target directory. Defaults to ....
    """
    directory, removed = os.listdir(folder), []
    for file in directory:
        file = os.path.join(folder, file)
        if file.split(".")[-1] in filetypes:
            removed.append(file)
            os.remove(file)


def mkdir(*paths: str, display: bool = False) -> None:
    """Makes directory if it does not exist.

    Args:
        paths (list): enter enter each individual arguments for each path (i.e., "path1", "path1", etc.)
        display (bool, optional): option to print its creation in terminal. Defaults to False.
    """
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)
            if display:
                print(f"Directory created: {path}")
        elif os.path.exists(path) and display:
            print("Directory already exists")


def unique(
    filename: str = ...,
    path: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ),  # CWD
    copy_pattern: str = "Run ",
) -> Tuple[str, int]:
    """Produces updating enumeration of consecutive file names

    Args:
        filename (str): original name of file. Defaults to ...
        path (str, optional): defualt directory for saving log files. Defaults to os.path.dirname(os.path.dirname(os.path.abspath(__file__))).
        copy_pattern (str): appended pattern. Defaults to "Run"

    Returns:
        str: filename with unique number identifier appended to original filename
    """
    # FIXME - fix rest argument for path
    base_name, ext = os.path.splitext(filename)
    unique_name, counter = filename, 1
    while os.path.exists(os.path.join(path, unique_name)):
        counter += 1
        unique_name = f"{base_name} ({copy_pattern}{counter}){ext}"

    return unique_name, counter


def filter(parent_folder: str = ..., file_type: str = ...) -> List[str]:
    """Fetches all files recursively in a desired directory and all its subdirectories.

    Args:
        parent_folder (str, optional): path to folder you want to parse. Defaults to ....
        file_type (str, optional): file extension you are searching for. Defaults to ....

    Returns:
        List of strings of absolute paths of every file that fits 'file_type.'
    """
    return glob.glob(parent_folder + "/**/" + file_type, recursive=True)


def join(*paths: str) -> str:
    """Joins paths

    Returns:
        str: joined paths
    """
    return os.path.join(*paths)
