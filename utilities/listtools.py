from random import shuffle
from typing import Any, Dict, Iterable, List, Literal, Sequence, Set, Tuple

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


def to_dictionary(
    keys_list: Set[str] = ..., values_list: List[Any] = ...
) -> Dict[Any, Any]:
    """
    Combines to lists into a single dictionary of key-value pairs. Both lists must be of the same length, and the list of keys must not contain any duplicates

    Args:
        keys_list (list, optional): list of assigned keys. Defaults to ....
        values_list (list, optional): list of corresponding values. Defaults to ....

    Returns:
        Dictionary of key-value pairs
    """
    return {key: value for key, value in zip(keys_list, values_list)}


def test_set(_list: Iterable = None):
    """
    Tests if a list is a set (i.e., containes only unique values). Finds unique values using `set()` then compares the length of the set with the length of the original list.

    Args:
        _list (Iterable=None): List to evaluate.

    Returns:
        Bool: Returns `True` if the length of the set eequals the length of the list, meaning the list contains all unqiue values, returns `False` otherwise.
    """
    return len(set(_list)) == len(_list)


def len_compare(_list1: Iterable = None, _list2: Iterable = None):
    """
    Compares the lenghts of two lists. Returns `True` is both lenghts are the same, otherwise retuns `False`.

    Args:
        _list (Iterable=None): List to evaluate.

    Returns:
        Returns `True` is both lenghts are the same, otherwise retuns `False`.
    """
    return len(_list1) == len(_list2)


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


def make_vec_comp_names(
    vector_types: list = None, components: list = None
) -> List[str]:
    """
    Creates a list of vector components for desired vectors. Used statically.

    Args:
        vector_types (list, optional): Letter component of vector (e.g., "B", "V"). Default is None.
        components (list, optional): Letter component of vector (e.g., "x", "y"). Default is None.

    Returns:
        List[str]: Returns a list of formatted vector component names as strings.

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


def unique_int_list(start: int = None, stop: int = None, step: int = None) -> int:
    """
    Creates shuffled list of integers at set range.

    Args:
        start (int): Range start. Defaults to None.
        stop (int): Range end. Defaults to None.
        step (int): Step of range. Defaults to None.

    Returns:
        List[int]: List of shuffled integers.
    """
    return shuffle(range(start, stop, range))
