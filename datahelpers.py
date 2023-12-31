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
- class ParseCfg
- function read_json
- function read_txt
- function write_to_excel
- function write_to_json
- function write_to_txt
"""

import json
import os
import warnings
from configparser import ConfigParser
from typing import Any, Callable, Dict, List, Literal, Sequence, Tuple
from zipfile import ZipFile

import numpy as np
import torch
from pandas import DataFrame, ExcelWriter

# from strfmts import osdate_time
# from userwarnings import MissingArgumentsWarning

_reduced_types = DataFrame | List[DataFrame] | Tuple[DataFrame]


def to_excel(
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


def df_to_json(
    data: DataFrame = None,
    save_as: str = None,
    mode: Literal["w", "wb"] = "w",
    cfg={"orient": "dict", "into": type(dict), "index": True},
):
    """
    Saves a Pandas DataFrame into a JSON file.

    Args:
        data (DataFrame): DataFrame you are saving. Default to None.
        save_as (string): Name of JSON file you are saving to. Default to None.
        mode (Literal["w", "wb"]): Mode you are saving the DataFrame with. Default to "w".
        cfg (Dict): Configuration dictionary for DataFrame -> Dictionary conversion. Default to None.
    """
    data = data.to_dict(**cfg)
    with open(save_as, mode) as file:
        json.dump(data, file)


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


def read_json(
    filename: str = None, sort_key: Any = None, *args, **kwargs
) -> Dict[Any, Any]:
    """
    Reads JSON file. Returns None if path does not exist.

    Args:
        filename (str, optional): name of JSON file to read. Defaults to None.

    Returns:
        dictionary: returns read JSON data
    """
    with open(filename, *args, **kwargs) as f:
        data = json.load(f) if os.path.exists(filename) else None
        if sort_key:
            return sorted(data, key=sort_key)
        else:
            return data


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
    extract_mode: Literal["folder", "lists"] = "folder",  # FIXME - not finished
    out_dir: str = None,
) -> None:
    """
    Extracts contents of a ZIP file.

    Args:
        zipped_file (str, optional): File path to zipped file. Defaults to None.
        read_mode (Literal[&quot;r&quot;], optional): File reading mode. Defaults to "r".
        extract_mode (Literal[&quot;folder&quot;, &quot;lists&quot;], optional): ZIP extraction mode. Defaults to "folder".
        out_dir (str, optional): Directory you want to save the extracted contents to. Defaults to None.
    """
    # TODO - finish the second half of this function
    with ZipFile(zipped_file, read_mode) as file:
        file.extractall(out_dir)


def save_dict2xml(
    data: Dict[str, Any] = None, save_as: str = None, mode: Literal["w", "wb"] = "wb"
) -> None:
    """
    Saves a dictionary to an XML file.

    Args:
        data (Dict[str, Any], optional): Dictionary that you want to save. Defaults to None.
        save_as (str, optional): Name you are saving the XML file as. Defaults to None.
        mode (Literal[&quot;w&quot;, &quot;wb&quot;], optional): File writing mode. Defaults to "wb".
    """
    data = data.encode()
    with open(save_as, mode) as file:
        file.write(data)


def extract_tar(tarfile: str = None, path: str = None) -> None:
    """
    Extracts data from a `.tar` file.

    Parameters
    ----------
    tarfile : str, optional
        Path to your `.tar` file, by default None
    path : str, optional
        Path where you want to save the data to, by default None
    """
    with tarfile.open(tarfile) as file:
        file.extractall(path)


def list2tensor(
    y: Sequence | np.array, sqz: int = 1, conv_type: Callable = torch.int64
) -> torch.Tensor:
    """
    Converts an array (or list) into a `PyTorch` tensor (`torch.Tensor`).

    Parameters
    ----------
    y : Sequence | np.array
        Sequence that you want to convert to a tensor.
    sqz : int, optional
        Squeeze value, by default 1
    conv_type : Callable, optional
        Type you want to convert the tensor values to, by default torch.int64

    Returns
    -------
    torch.Tensor
        Final tensor from sequence.
    """
    y = y.to_numpy()
    y = torch.Tensor(y)
    y = y.squeeze(sqz)
    y = y.type(conv_type)
    return y


def conv2str(df: DataFrame = None, dtype: str = "str"):
    """
    Converts all columns of a given DataFrame into a desired data type.

    Parameters
    ----------
    df : DataFrame, optional
        DataFrame that you want to convert, by default None
    dtype : str, optional
        Data type you want to convert the columns to, by default "str"
    """
    for colname in df.columns:
        try:
            df[colname] = df[colname].astype(dtype)
            print(f"'{colname}' converted to {dtype}")
        except:
            print(f"'{colname}' conversion failed")


def combine_list(strings: list) -> str:
    """
    Combineds a list of strings into a single string.

    Parameters
    ----------
    strings : list
        List of strings that you want to convert into a single string.

    Returns
    -------
    str
        Final combined string.
    """
    return "".join(strings).strip()


def normalize(matrix: np.array | Sequence = None) -> np.array:
    """
    Divides matrix (or array) my its norm for normalization.

    Parameters
    ----------
    matrix : np.array | Sequence, optional
        Matrix (or array) that you want to normalize, by default None

    Returns
    -------
    np.array
        Normalized array or matrix.
    """
    norm = np.linalg.norm(matrix)
    return matrix / norm


class ParseConfig(ConfigParser):
    # FIXME - NOT WORKING
    def __init__(self, filepath: str = None) -> None:
        self.path = filepath

        self._FILE = ConfigParser(self.path)
        self._parsed_file = self._FILE.read()

    def get_val(
        self,
        section: str = None,
        key: str = None,
        _type: Literal["str", "bool", "int", "float"] = None,
    ) -> Any:
        if not _type:
            return None

        match _type:
            case "str":
                return self._parsed_file.get(section, key)
            case "bool":
                return self._parsed_file.getboolean(section, key)
            case "int":
                return self._parsed_file.getint(section, key)
            case "float":
                return self._parsed_file.getfloat(section, key)

    @property
    def cfgsections(self):
        return self._parsed_file.sections()
