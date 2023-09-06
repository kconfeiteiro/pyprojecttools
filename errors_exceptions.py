"""
User defined errors and exceptions.

Functions
---------
function tryexcept

Classes
-------
class NotASetError
	method __init__
		variable args
class IncompatibleArugmentsWarning
    pass
class MissingArgumentError
  method __init__
        variable functionname
    method __str__
class FileReadError
	method __init__
		variable filename
	method __str__
class MissingMethod
	method __init__
		variable classname
		variable method
	method __str__
class KeyErrorWarning
	method __init__
		variable args

"""

import traceback
from typing import Any, Callable


class NotASetError(TypeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def tryexcept(func):
    def wrapper(*args, **kwargs):
        try:
            result = yield from func(*args, **kwargs)
            yield result
        except Exception as e:
            print(e)
            result = None
            yield result
        return result

    return wrapper


class IncompatibleArugmentsWarning(UserWarning):
    pass


class KeyErrorWarning(UserWarning):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MissingArgumentError(ValueError):
    def __init__(self, function: object = None) -> None:
        super().__init__()
        self.function = function
        self._funcname = self.function.__name__
        self.tb = traceback.format_exc()
        self._msg = f"Missing arguments for {self._funcname}"

    def __str__(self) -> str:
        return f"{self._msg}\n{self.tb}"


class FileReadError(ValueError):
    def __init__(self, filename: str = None):
        self.filename = filename
        self.tb = traceback.format_exc()
        self.msg = f"Error reading file: {self.filename}"

    def __str__(self) -> str:
        return f"{self.msg}\n{self.tb}"


class MissingMethodError(Exception):
    def __init__(self, classname: Any = None, method: Callable = None) -> None:
        self.classname = classname.__name__
        self.method = method.__name__
        self.tb = traceback.format_exc()
        self._msg = f"Method {self.method} in {self.classname} must be ran prior."

    def __str__(self):
        return f"{self._msg}\n{self.tb}"


class MissingDataError(ValueError):
    def __init__(self, data) -> None:
        self._data = data
        self.tb = traceback.format_exc()
        self._msg = f"Invalid dataset shape, '{self._data.shape}'."

    def __str__(self) -> str:
        return f"{self._msg}\n{self.tb}"
