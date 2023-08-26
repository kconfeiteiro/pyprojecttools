"""Module for abstract classes (architectures) that are common and uncommon, for general usage."""

from enum import Enum
from typing import TypedDict


class RANGE(Enum):
    """
    Value range for data reduction.

    Value range:
    - (low) `RANGE.low` = 0.25
    - (med) `RANGE.med` = 0.5
    - (high) `RANGE.high` = 0.75
    """

    low = 0.25
    med = 0.5
    high = 0.75


class PltCfg(TypedDict):
    """
    Configuration dictionary for plot objects.

    Args:
        size (str): Figure size
        save_as (str): Filename for saved plot
        reduce_data (RANGE | int | float): Amount to reduce data.
    """

    size: str
    save_as: str
    reduce_data: RANGE | int | float
    output_dir: str | None
