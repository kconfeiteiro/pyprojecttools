"""Custom iterators for control flow."""

import os
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


class DirectoryFileIterator:
    """
    Iterate through files in a directory with their absolute paths.

    Attributes:
        directory_path (type): Path to iterate through.
        files (type): Files in that directory.
        index (type): Iteration index.

    Args:
        directory_path (undefined):

    """

    def __init__(self, directory_path: str = None):
        self.directory_path = directory_path
        self.files = os.listdir(directory_path)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        file_path = os.path.join(self.directory_path, self.files[self.index])
        self.index += 1
        return file_path
