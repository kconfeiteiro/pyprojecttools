""" Tools related to data manipulation/operations """


import warnings
from typing import Any, List, Literal, Tuple, Union

from pandas import DataFrame

from userwarnings import MissingArgumentsWarning


def reduce_df(
    data: DataFrame = None,
    percent: float = None,
    save_type: Literal["list", "tuple"] = None,
) -> DataFrame | List[DataFrame] | Tuple[DataFrame]:
    """

    Reduces size of `pd.DataFrame` input based on decimal-representation of what percentage of the original dataset the returned data set should be. Orginial dataset will be returned if parameters are not correctly set (as a safeguard). User is warned if arguments are missing.

    Additional notes:
    - Your data can be returned as a list or tuple of the columns

    Parameters
    ----------
    data : DataFrame, optional
        Original dataset, by default None
    percent : float, optional
        Percentage of `data` that you want returned, by default None

    Returns
    -------
    DataFrame
        Shortened dataframe.
    """
    if not (data or percent):
        warnings.warn(
            "'data' and 'percent' must both me used. Original dataset will be returned if inputted, otherwise, None will be returned.",
            MissingArgumentsWarning,
        )
        return data if data and not percent else None
    elif data and percent:
        new_df = data.head(int(data.shape[0] * percent))
        cols_list = [new_df[col] for col in new_df.columns]
        returns = {"list": cols_list, "tuple": tuple(cols_list)}
        return returns.get(save_type, new_df)


def pull_columns(data: Any = None, *cols, as_tuple: bool = False) -> Union[List, Tuple]:
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
