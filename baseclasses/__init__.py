"""Module for abstract classes (architectures) that are common and uncommon, for general usage."""

from typing import Iterable


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
