""" Tools related to data manipulation/operations """


import warnings
from typing import Any, List, Literal, Tuple, Union

from pandas import DataFrame
from userwarnings import MissingArgumentsWarning


def reduce_df(
    data: DataFrame = None,
    percent: float = None,
    save_type: Literal["list", "tuple", "dataframe"] = None,
) -> DataFrame | List[DataFrame] | Tuple[DataFrame]:
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
        warnings.warn(_msg, MissingArgumentsWarning)
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
