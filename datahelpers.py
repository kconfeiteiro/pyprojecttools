"""
Data I/O operations (reading, saving, etc.).

Script Information
------------------
- Contact: confeitk@outlook.com
- Workspace: pyprojecttools
- FIlename: datahelpers.py
- Date: September 29, 2023


Functions
---------
- function read_json
- function read_txt
- function write_to_excel
- function write_to_json
- function write_to_txt
"""

import json
import os
import warnings
from typing import Any, Dict, List, Literal, Sequence, Tuple
from zipfile import ZipFile

from pandas import DataFrame, ExcelWriter

# from strfmts import osdate_time
# from userwarnings import MissingArgumentsWarning

_reduced_types = DataFrame | List[DataFrame] | Tuple[DataFrame]


def to_excel(
    # save_as: str = f"untitled_excel_sheet-{osdate_time}.xlsx",
    save_as: str = None,
    df: DataFrame | List[DataFrame] = None,
    sheetnames: str | List[str] = "Main",
    index: bool = False,
    **kwargs,
):
    """
    Builds an Microsoft Excel file (`.xlsx` or `.xls`) from single or multiple Pandas dataframes (`pd.DataFrame` object). In the latter case, it will create separate pages for each dataframe using a list of sheetnames. If no sheetname list is provided, an enumerated list will be used.

    Args:
        save_as (str, optional): what you want to name the saved file. Defaults to f"untitled_excel_sheet-{osdate_time}.xlsx".
        df (DataFrame, optional): single dataframe or list of dataframes you want to write to file. Defaults to None.
        sheetname (Union[str, List], optional): name or list of names you want to name each excel sheet page. Defaults to 'Main'.
        index (bool, optional): option to write the index of each dataframe. Defaults to False.
    """
    with ExcelWriter(save_as) as writer:
        if isinstance(sheetnames, List[DataFrame]):
            for data, sheetnames in zip(df, sheetnames):
                data.to_excel(writer, sheet_name=sheetnames, index=index, **kwargs)
        else:
            df.to_excel(writer, sheet_name=sheetnames, index=index, **kwargs)


def to_txt(
    save_as: str = None,
    lines: str | List[str] = None,
    mode: Literal["w", "wb", "a"] = "w",
    **kwargs,
):
    """
    Writes string or list of strings to a text file.

    Args:
        save_as (str, optional): name to save file as. Defaults to None.
        lines (Union[str, List[str]], optional): string or list of strings to save to file. Defaults to None.
        mode (literal, optional): write mode for ExcelWriter. Defaults to 'w'.
    """
    with open(save_as, mode=mode, **kwargs) as file:
        if isinstance(lines, str):
            file.write(lines)
        else:
            for line in lines:
                file.write(line)
        file.close()


def to_json(
    save_as: str = None,
    dict_to_save: Dict = None,
    mode: Literal["w", "wb"] = "w",
    **kwargs,
):
    """
    Writes a dictionary to a JSON file

    Args:
        save_as (str, optional): name to save file as. Defaults to None.
        dict_to_save (Dict, optional): dictionary you want to write to the JSON file. Defaults to None.
        mode (literal, optional): writing mode. Defaults to 'w'.
    """
    with open(save_as, mode) as file:
        json.dump(dict_to_save, file, **kwargs)


def read_txt(
    filename: str = None, mode: Literal["r", "rb"] = "r", **kwargs
) -> List[str]:
    """
    Reads text file. Returns None if path does not exist.

    Args:
        filename (str, optional): file name to read. Defaults to None.
        mode (literal, optional): reading mode. Defaults to 'r'.

    Returns:
        list: returns list of strings of line read
    """
    with open(filename, mode=mode, **kwargs) as file:
        return file.readlines() if os.path.exists(filename) else None


def read_json(filename: str = None, *args, **kwargs) -> Dict[Any, Any]:
    """
    Reads JSON file. Returns None if path does not exist.

    Args:
        filename (str, optional): name of JSON file to read. Defaults to None.

    Returns:
        dictionary: returns read JSON data
    """
    with open(filename, *args, **kwargs) as f:
        return json.load(f) if os.path.exists(filename) else None


def reduce_df(
    data: DataFrame = None,
    percent: float = None,
    save_type: Literal["list", "tuple", "dataframe"] = None,
) -> _reduced_types:
    """
    Reduces size of `pd.DataFrame` input based on decimal-representation of what percentage of the original dataset the returned data set should be. Orginial dataset will be returned if parameters are not correctly set (as a safeguard). User is warned if arguments are missing.

    Notes:
    - Your data can be returned as a list or tuple of the columns.

    Args:
        data (`DataFrame`): Original dataset, by default None
        percent (float): Percentage of `data` that you want returned, by default None
        save_type (literal, optional): Return shortened `DataFrame` as a `tuple` or `list` of the columns, returns `new_df` if left `None` or `"dataframe"`.

    Returns:
        DataFrame: Shortened `DataFrame` as a tuple or list of the columns, or left as a `DataFrame`.
    """
    if not (data or percent):
        _msg = "'data' and 'percent' must both me used. Original dataset will be returned if inputted, otherwise, None will be returned."
        # warnings.warn(_msg, MissingArgumentsWarning)
        return data if data and not percent else None
    elif data and percent:
        new_df = data.head(int(data.shape[0] * percent))
        df_list = [new_df[col] for col in new_df.columns]
        returns = {"list": df_list, "tuple": tuple(df_list), "dataframe": new_df}
        return returns.get(save_type, new_df)


def pull_columns(data: Any = None, *cols, as_tuple: bool = False) -> List | Tuple:
    """
    Method for pulling specific columns of dataframe, as list or tuple of said columns.

    Args:
        data (Any, optional): data to pull from (as a Pandas dataframe). Defaults to None.
        tuple (bool, optional): option to return a tuple of pulled columns. Defaults to False.

    Returns:
        list or tuple: returns targeted columns as a list or tuple
    """
    pulled = (data[col] for col in cols)
    return pulled if as_tuple else list(pulled)


def zip_folder(
    zipped_filename: str = None,
    to_zip: Sequence[str] | str = None,
    mode: Literal["w", "x", "a"] = "w",
) -> None:
    """
    Zip files to folder. Enter a path to a dirctory, or a list of paths to files to zip.

    Args:
        zipped_filename (str, optional): Name of zipped folder. Defaults to None.
        to_zip (Sequence[str] | str, optional): Path to directory or list of paths to zip. Defaults to None.
        mode (literal["w", "x", "a"], optional): Zipping mode. Defaults to "w".

    Notes:
    - Zipping modes:
        - `w` for writing to a new file
        - `x` for referring to an existing file.
        - `a` for appending to an existing file.
    """
    with ZipFile(zipped_filename, mode) as file:
        files_list = list(to_zip) if os.path.isdir(to_zip) else to_zip
        for _file in files_list:
            file.write(_file)


def zip_extract(
    zipped_file: str = None,
    read_mode: Literal["r"] = "r",
    extract_mode: Literal["folder", "lists"] = "folder",
    out_dir: str = None,
) -> List[str] | None:
    with ZipFile(zipped_file, read_mode) as file:
        file.extractall(out_dir)
