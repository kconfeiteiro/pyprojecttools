import ast
import json
import os
import re
from typing import Any, Dict, List, Literal, Sequence, Tuple, Union

import num2word
import pandas as pd

from pyprojecttools.custom_dtypes import Dataframe

""" Data I/O operations (reading, saving, etc.) """


def write_to_excel(
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


def read_txt(
    filename: str = ..., mode: Literal["r", "rb"] = "r", **kwargs
) -> List[str]:
    """Reads text file

    Args:
        filename (str, optional): file name to read. Defaults to ....
        mode (literal, optional): reading mode. Defaults to 'r'.

    Returns:
        list: returns list of strings of line read
    """
    with open(filename, mode=mode, **kwargs) as file:
        return file.readlines()


def read_json(filename: str = ..., *args, **kwargs) -> Dict[Any, Any]:
    """Reads JSON file

    Args:
        filename (str, optional): name of JSON file to read. Defaults to ....

    Returns:
        dictionary: returns read JSON data
    """
    assert os.path.exists(filename), "File not found"
    with open(filename, *args, **kwargs) as f:
        return json.load(f)


def write_txt(
    save_as: str = ...,
    content: Union[str, List[str]] = ...,
    mode: Literal["w", "wb"] = "w",
    *args,
    **kwargs,
):
    """Writes str or list of strings to a text file

    Args:
        save_as (str, optional): name of saved file. Defaults to ....
        content (Union[str, List[str]], optional): list or list of strings to write. Defaults to ....
        mode (literal, optional): writing mode. Defaults to "w".
    """
    with open(save_as, mode, *args, **kwargs) as file:
        assert (
            type(content) in [list, List[str]],
            "Content is of wrong format, needs to be string or list of string",
        )

        if isinstance(content, list):
            for line in content:
                file.write(line)
                file.write("\n")
        else:
            file.write(content)


def pull_columns(data: Any = None, *cols, as_tuple: bool = False) -> Union[List, Tuple]:
    """Method for pulling specific columns of dataframe, as list or tuple of said columns.

    Args:
        data (Any, optional): data to pull from (as a Pandas dataframe). Defaults to None.
        tuple (bool, optional): option to return a tuple of pulled columns. Defaults to False.

    Returns:
        list or tuple: returns targeted columns as a list or tuple
    """
    pulled = (data[col] for col in cols)
    return pulled if as_tuple else list(pulled)


""" Helper fuctions for any mutuable or immutable sequence """


def map_matrix(m: int = ..., n: int = ...) -> List[Tuple[int, int]]:
    """Creates a flattened list of matrix indexies (for subplots) for easy plotting.

    Args:
        m (int, optional): number of rows. Defaults to ....
        n (int, optional): number of columns. Defaults to ....

    Returns:
        A list of tuples representing the location of each subplot
    """
    return [(i + 1, j + 1) for i in range(m) for j in range(n)]


def combine_lists(
    list1: Sequence = None,
    list2: Sequence = None,
    combine_as: Literal["tuple", "list"] = "list",
):
    """Combines to lists into a single lists with each corresponding item in one tuple.

    Args:
        list1 (sequence, optional): first list to combine. Defaults to ....
        Sequence (sequence, optional): second list to combine. Defaults to ....

    Returns:
        Combined lists as a single lists of tuples
    """
    combined = [(i, j) for i, j in zip(list1, list2)]
    return tuple(combined) if combine_as == "tuple" else combined


def combine_to_dictionary(
    keys_list: List[Any] = ..., values_list: List[Any] = ...
) -> Dict[Any, Any]:
    """Combines to lists into a single dictionary of key-value pairs. Both lists must be of the same length, and the list of keys must not contain any duplicates

    Args:
        keys_list (list, optional): list of assigned keys. Defaults to ....
        values_list (list, optional): list of corresponding values. Defaults to ....

    Returns:
        Dictionary of key-value pairs
    """
    return {key: value for key, value in zip(keys_list, values_list)}


def combine_list_strings(
    primary_list: List[Any] = ..., secondary_list: List[Any] = ...
) -> List[str]:
    """Combines two strings into a single list of strings. Optional formats to be added.

    Args:
        primary_list (list, optional): primary list to combine. Defaults to ....
        secondary_list (list, optional): secondary list to combine. Defaults to ....

    Returns:
        List of strings combined from the two lists
    """
    return [
        "{} ({})".format(str(l1), str(l2))
        for l1, l2 in zip(primary_list, secondary_list)
    ]


""" Helper fuctions for strings operations/manipulation """


def numToWord(num: int = ...) -> str:
    """Converts an integer to its corresponding word-phrase, i.e., 23 -> 'twenty three'

    Args:
        num (int, optional): number you want to convert. Defaults to ....

    Returns:
        str: corresponding word-phrase
    """
    return num2word.word(num).lower()


def format_long(string: str = ..., cut: float = 0.50) -> str:
    """Reformats long strings based on 'cut' percentage and replaces former half with an ellipse.

    Args:
        string (str, optional): string you want to modify. Defaults to ....
        cut (float, optional): percentage of the first half of the string you want to reduce. Defaults to 0.50.

    Returns:
        str: formatted string
    """
    return "...{}".format(string[round(len(string) * cut) :])


def shorten(*cols, new_len: int = None) -> Tuple[Any]:
    """Returns a tuple of shortened columns. This was written for simple use with testing plotting functions

    Args:
        new_len (int, optional): new desired length. Defaults to None.

    Returns:
        tuple: tuple list of shortened data frames
    """
    return (col[:new_len] for col in cols)


def parse_kwarg_string(kwargs_string: str = ...) -> Dict[str, Any]:
    """Parses a string of of kwargs (keyword arguments, e.g., "delim_whitespace=True, comment='#'") into a dictionary of the kwargs (particularly for use with a GUI). NOTE: Does not do well parsing strings that contain list substrings.

    Args:
        kwargs_string (str, optional): string containing keywords to parse. Defaults to ....

    Returns:
        dict: dictionary of parsed keyword arguments
    """
    pairs = kwargs_string.split(",")
    arguments = [pair.split("=") for pair in pairs]
    kwargs_dict = {}
    for arg in arguments:
        keyword = arg[0].strip()
        value = arg[1].strip()
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            value = value.strip("'")
        kwargs_dict[keyword] = value
    return kwargs_dict


def strmatch(pattern: str = ..., string: str = ..., **kwargs) -> bool:
    """Static method for determining if a string matches a Regex pattern

    Args:
        pattern (str, optional): pattern to match to. Defaults to ....
        string (str, optional): string you are matching. Defaults to ....

    Returns:
        bool: returns True if it matches, False if it doesn't
    """
    return bool(re.search(pattern, string, **kwargs))


def make_vec_comp_names(
    vector_types: list = None, components: list = None
) -> List[str]:
    """Creates list of vector components for desired vectors for easier automated plotting.

    Args:
        vector_types (list, optional): letter denotion of vector (i.e., "B', "V", etc.). Defaults to None.
        components (list, optional): chosen vector componenets (i.e., "x", "y", "y"). Defaults to None.

    Returns:
        List[str]: list of strings for corresponding vector components

    Example:
        >>> vector_types = ['position', 'velocity']
        >>> components = ['x', 'y', 'z']
        >>> output = make_vec_comp_names(vector_types, components)
        >>> print(output)
        >>> ['POSITION_x', 'POSITION_y', 'POSITION_z', 'VELOCITY_x', 'VELOCITY_y', 'VELOCITY_z']
    """
    return [
        f"{vec.upper()}_{axis.lower()}" for vec in vector_types for axis in components
    ]
