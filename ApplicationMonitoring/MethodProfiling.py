import time
from typing import Any, Tuple, Union


""" Tracking method executions, method runtimes, etc. """


class Timer:
    def __init__(self, func):
        """Independent decorator for timing function executions. Can be used with Logger class.

        Args:
                func (callable): function automatically inputted when decorator is called
        """
        self.func = func

    def __call__(
        self, return_result: bool = False, *args, **kwargs
    ) -> Union[Tuple[float, Any], float]:
        """Calculates function execution time.

        Args:
                return_result (bool, optional): option to return result of function. Defaults to False.

        Returns:
                tuple[float, Any] or float: returns execution or addition of the function's result
        """
        start_time = time.time()
        result = self.func(*args, **kwargs)
        execution_time = time.time() - start_time

        if return_result:
            return execution_time, result
        else:
            return execution_time


class Counter:
    def __init__(self):
        """Decorator for counting number of function executions. Updates automatically. Can be used with Logger class."""
        self.count = 0

    def __call__(self) -> int:
        """Counts number of times a function is called. Updates automatically.

        Returns:
                int: function call-count
        """
        self.count += 1
        return self.count
