import ast
import re
from typing import Any, Dict, List, Tuple

import num2word


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
    """
    Creates list of vector components for desired vectors for easier automated plotting.

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


def numToWord(num: int = ...) -> str:
    """
    Converts an integer to its corresponding word-phrase, i.e., 23 -> 'twenty three'

    Args:
        num (int, optional): number you want to convert. Defaults to ....

    Returns:
        str: corresponding word-phrase
    """
    return num2word.word(num).lower()


def format_long(string: str = ..., cut: float = 0.50) -> str:
    """
    Reformats long strings based on 'cut' percentage and replaces former half with an ellipse.

    Args:
        string (str, optional): string you want to modify. Defaults to ....
        cut (float, optional): percentage of the first half of the string you want to reduce. Defaults to 0.50.

    Returns:
        str: formatted string
    """
    return "...{}".format(string[round(len(string) * cut) :])


def strmatch(pattern: str = ..., string: str = ..., **kwargs) -> bool:
    """
    Static method for determining if a string matches a Regex pattern

    Args:
        pattern (str, optional): pattern to match to. Defaults to ....
        string (str, optional): string you are matching. Defaults to ....

    Returns:
        bool: returns True if it matches, False if it doesn't
    """
    return bool(re.search(pattern, string, **kwargs))
