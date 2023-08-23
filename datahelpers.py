""" Data I/O operations (reading, saving, etc.) """

import json
import os
from typing import Any, Dict, List, Literal

from pandas import DataFrame, ExcelWriter

from .strfmts import osdate_time


def write_to_excel(
    save_as: str = f"untitled_excel_sheet-{osdate_time}.xlsx",
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
        if isinstance(sheetnames, list):
            for data, sheetnames in zip(df, sheetnames):
                data.to_excel(writer, sheet_name=sheetnames, index=index, **kwargs)
        else:
            df.to_excel(writer, sheet_name=sheetnames, index=index, **kwargs)


def write_to_txt(
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


def write_to_json(
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
