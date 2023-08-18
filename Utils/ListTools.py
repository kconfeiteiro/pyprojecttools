from typing import Any, Dict, List, Literal, Sequence, Tuple

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
