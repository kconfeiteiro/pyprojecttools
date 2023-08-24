"""Module for abstract classes (architectures) that are common and uncommon, for general usage."""

from enum import Enum
from typing import Iterable, TypedDict


class ObjIterator:
    """
    `ObjIterator`: Permits iterations through objects for child classes.

    Attributes:
        items (type): Object to iterate.
        index (type): Index counted during iteration.

    Args:
        items (Iterable=None): Object to iterate.

    """

    def __init__(self, items: Iterable = None):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        self.index += 1
        return self.items[self.index]


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
    size: str
    save_as: str
    reduce_data: RANGE | int | float
