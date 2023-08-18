from typing import Any, List, Tuple, Union


""" Tools related to data manipulation/operations """


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
