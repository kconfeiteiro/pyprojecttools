"""User defined errors and exceptions."""

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


class MissingArgumentError(ValueError):
    def __init__(self, functionname: object = None) -> None:
        super().__init__()
        self.functionname = functionname
        self._funcname = self.functionname.__name__

    def __str__(self) -> str:
        return


class FileReadError(ValueError):
    def __init__(self, filename: str = None):
        self.filename = filename
        self.tb = traceback.format_exc()
        self.msg = f"Error reading file: {self.filename}"

    def __str__(self) -> str:
        return f"{self.msg}\n{self.tb}"


class MissingMethod(Exception):
    def __init__(self, classname: Any = None, method: Callable = None) -> None:
        self.classname = classname.__name__
        self.method = method.__name__

    def __str__(self):
        return f"Method {self.method} in {self.classname} must be ran prior."


class KeyErrorWarning(UserWarning):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
