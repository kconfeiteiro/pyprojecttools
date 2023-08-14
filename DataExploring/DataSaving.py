import json
from typing import (
    Dict,
    List,
    Literal,
    Union,
)

import pandas as pd

from CustomDatatypes.TabularDataStructures import Dataframe

""" for anything related to saving data (in any format)"""


def build_xl(
    save_as: str = ...,
    df: Union[Dataframe, List[Dataframe]] = ...,
    sheetname: Union[str, List[str]] = "Main",
    index: bool = False,
    **kwargs,
):
    """Builds an Microsoft Excel file from single or multiple Pandas dataframes. In the latter case, it will create separate pages for each dataframe

    Args:
        save_as (str, optional): what you want to name the saved file. Defaults to ....
        df (Dataframe, optional): single dataframe or list of dataframes you want to write to file. Defaults to ....
        sheetname (Union[str, List], optional): name or list of names you want to name each excel sheet page. Defaults to 'Main'.
        index (bool, optional): option to write the index of each dataframe. Defaults to False.
    """
    with pd.ExcelWriter(save_as) as writer:
        if isinstance(sheetname, list):
            for data, sheetname in zip(df, sheetname):
                data.to_excel(writer, sheet_name=sheetname, index=index, **kwargs)
        else:
            df.to_excel(writer, sheet_name=sheetname, index=index, **kwargs)

    print(f"File has been written to {save_as}")


def write_to_txt(
    save_as: str = ...,
    lines: Union[str, List[str]] = ...,
    mode: Literal["w", "wb", "a"] = "w",
    **kwargs,
):
    """Writes string or list of strings to a text file

    Args:
        save_as (str, optional): name to save file as. Defaults to ....
        lines (Union[str, List[str]], optional): string or list of strings to save to file. Defaults to ....
        mode (literal, optional): write mode for ExcelWriter. Defaults to 'w'.
    """
    with open(save_as, mode=mode, **kwargs) as file:
        if isinstance(lines, str):
            file.write(lines)
        else:
            for line in lines:
                file.write(line)
        file.close()

    print(f"File has been written to {save_as}")


def write_to_json(
    save_as: str = ...,
    dict_to_save: Dict = None,
    mode: Literal["w", "wb"] = "w",
    **kwargs,
):
    """Writes a dictionary to a JSON file

    Args:
        save_as (str, optional): name to save file as. Defaults to ....
        dict_to_save (Dict, optional): dictionary you want to write to the JSON file. Defaults to None.
        mode (literal, optional): writing mode. Defaults to 'w'.
    """
    with open(save_as, mode) as file:
        json.dump(dict_to_save, file, **kwargs)

    print(f"File has been written to {save_as}")
