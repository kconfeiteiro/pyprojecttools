"""
Sorting, deleting, copying files, and dealing with directories

Functions:
- function `delete_filetype`
- function `file_filter`
- function `joinpths`
- function `mkdirectory`
- function `uniquefilename`
"""
import glob
import os
from typing import List, Tuple
from utilities.strtools import num_to_word


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


def mkdirectory(*paths: str, display: bool = False) -> None:
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


def uniquefilename(
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

    return (unique_name, counter)


def file_filter(parent_folder: str = ..., file_type: str = ...) -> List[str]:
    """Fetches all files recursively in a desired directory and all its subdirectories.

    Args:
        parent_folder (str, optional): path to folder you want to parse. Defaults to ....
        file_type (str, optional): file extension you are searching for. Defaults to ....

    Returns:
        List of strings of absolute paths of every file that fits 'file_type.'
    """
    return glob.glob(parent_folder + "/**/" + file_type, recursive=True)


def joinpths(*paths: str) -> str:
    """Joins paths.

    Returns:
        str: joined paths
    """
    return os.path.join(*paths)


def listdir(path: str = None) -> List[str]:
    """
    Lists all files in a directory (not recursive).

    Args:
        path (str, optional): Path to directory to list. Defaults to None.

    Returns:
        List[str]: List of file in said directory.
    """
    return glob.glob(pathname=path)


def find_last_file(
    path: str = ...,
    keyword: str = None,
    fetch: int = None,
    usetime: bool = False,
    showcase: bool = False,
):
    """
    Finds the last files in a directory depending on keyword or just last integer-amount of files.

    Parameters
    ----------
    path : str, optional
        Path to directory, by default ...
    keyword : str, optional
        Keyword to search directory, by default None
    fetch : int, optional
        Integer amount of (last) files to fetch, by default None
    usetime : bool, optional
        Option to find the files if based on their times, by default False
    showcase : bool, optional
        Option to print the findings (if not already done manually), by default False

    Returns
    -------
    List
        List of files found (as absolute paths).
    """
    if usetime:
        files = os.listdir(path)
        paths = [
            os.path.join(path, basename).replace(os.path.sep, "/") for basename in files
        ]
        temp = max(paths, key=os.path.getctime).replace(os.path.sep, "/")
        temp = os.path.basename(temp)
        print(f"Returned last file using key:", temp)
        return temp
    else:
        temp = os.listdir(path)
        if keyword is not None:
            try:
                temp = [ind for ind in temp if keyword in ind]
                if showcase:
                    [
                        print(f"Found '{item}' in '{path}' with keyword '{keyword}'")
                        for item in temp
                    ]
            except:
                print(f"No items found in '{path}' with keyword '{keyword}'")

        if fetch:
            temp = temp[-fetch:]
            if fetch == 0:
                print(f"Returned last file")
            else:
                if fetch > len(temp):
                    number = num_to_word(abs(fetch))
                    number1 = num_to_word(len(temp))

                    if keyword and showcase:
                        _msg = f"Returning last {number1} files with keyword '{keyword}': {temp}"
                        print(_msg)
                    elif showcase:
                        _msg = f"Returning last {number1}: {temp} "
                        print(_msg)
                else:
                    number = num_to_word(abs(fetch))
                    if showcase:
                        print(
                            f"Returned last {number} files with keyword '{keyword}': {temp}"
                            if keyword
                            else f"Returning last {number} files:",
                            temp,
                        )

            return temp
        else:
            try:
                lastfile = temp[-1]
                if showcase:
                    print(f"Returned last file: '{lastfile}'")
                return lastfile
            except:
                if showcase:
                    print(f"No items found in '{path}' with keyword '{keyword}'")

                return None
