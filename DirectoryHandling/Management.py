import json
import os
from typing import Any, Dict, List, Literal, Union


""" For anything realated to reading data from file or directory """


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
    **kwargs
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
