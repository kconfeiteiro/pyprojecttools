import glob
import os
from typing import (Any, Callable, Dict, List, Literal, NewType, Tuple, Type,
                    TypeVar, Union)

from line_profiler import LineProfiler

""" For anything related to line-profiling (currently untested) """

class LineProfiler:

	def __init__(
		self,
		func: Callable = ...,
		line_profiler: Callable = LineProfiler(),
		log_filename: str = None,
		pdf_filename: str = None
	):
		"""Line profiler

		Args:
			func (Callable, optional): target function. Defaults to ....
			line_profiler (Callable, optional): line profiler object (from line_profiler). Defaults to LineProfiler().
			log_filename (str, optional): name to save log file as. Defaults to None.
			pdf_filename (str, optional): name to save PDF report as (not working). Defaults to None.
		"""
		self.func = func
		self.line_profiler = line_profiler
		self.log_filename = log_filename
		self.pdf_filename = pdf_filename

	def __call__(self, *args, **kwargs):
		self.line_profiler.enable_by_count()
		result = self.func(*args, **kwargs)
		self.line_profiler.disable_by_count()

		# Write profiling statistics to log file
		self.line_profiler.print_stats(stream=open(self.log_filename, 'w'))

		# TODO: add option to create PDF report (make cumulative)
		# TODO: integrate logging from Logging.py
		return result