
from typing import (Any, Callable, Dict, List, Literal, NewType, Tuple, Type,
                    TypeVar, Union)

from memory_profiler import profile as memory_profile


""" For memory profiling (currently untested) """

class MemoryProfiler:

	def __init__(
		self,
		func: Callable = ...,
		memory_profiler: Callable = memory_profile(),
		log_filename: str = ...

	):
		"""Function decorator for memory profiling

		Args:
			func (Callable, optional): target function. Defaults to ....
			memory_profiler (Callable, optional): memory profiler object (from memory_profiler). Defaults to memory_profile().
			log_filename (str, optional): filename to save log file. Defaults to ....
		"""
		self.func = func
		self.memory_profiler = memory_profiler
		self.log_filename = log_filename

	def __call__(self, *args, **kwargs):
		self.memory_profiler.enable_by_count()
		result = self.func(*args, **kwargs)
		self.memory_profiler.disable_by_count()

		# Write memory profiling statistics to log file
		self.memory_profiler.print_stats(stream=open(self.log_filename, 'w'))
		return result