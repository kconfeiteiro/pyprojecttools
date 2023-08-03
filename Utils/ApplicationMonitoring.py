import code
import cProfile
import doctest
import logging
import pdb
import unittest
from typing import (Any, Callable, Dict, List, Literal, Tuple, Type, TypeVar,
                    Union)

import hydra
import pylint.lint
import pytest
from line_profiler import LineProfiler
from memory_profiler import profile as memory_profile
from pysnooper import snoop

from FileDataHandeling import FileWriting as fw
from FileSorting import FileSorting as fs
from Tools import Tools as t

''' for anything related to 'application monitoring'; tracking memory usage, execution times, etc. '''

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


class Lint:

	def __init__(self, filepath: str = ...) -> None:
		"""For linting a Python script file.

		Args:
			filepath (str, optional): path to file you want to lint. Defaults to ....
		"""
		self.filepath = filepath
		self.linting_results = None

	def process(
     	self,
		filename: str = None,
		mode: Literal['r', 'rb'] = 'r',
		exitl: bool = False,
    	do_exitl: bool = False,
    	reporter: Any = None,
    	stdin: Any = ...,
		write_to_text: str = ...,
		*args,
  		**kwargs
    ):
		"""Processes linting for desired script

		Args:
			filename (str, optional): name of file you want to lint. Defaults to None.
			mode (literal, optional): file reading mode. Defaults to 'r'.
			exitl (bool, optional): see pylint documentation. Defaults to False.
			do_exitl (bool, optional): see pylint documentation. Defaults to False.
			reporter (Any, optional): see pylint documentation. Defaults to None.
			stdin (Any, optional): see pylint documentation. Defaults to ....
			write_to_text (str, optional): option to write results to text. Defaults to ....
		"""
		code = Lint.parse_code(filename, mode)
		self.linting_results = pylint.lint.Run(
      		["-"],
        	exit=exitl,
         	do_exit=do_exitl,
          	reporter=reporter,
           	stdin=stdin,
            *args,
            **kwargs
        )

		if write_to_text:
			fw.write_txt(write_to_text, content=self.linting_results)


	@staticmethod
	def parse_code(filename: str = ..., mode: Literal['r', 'rb'] = 'r') -> Any:
		"""Static function for parsing a Python script

		Args:
			filename (str, optional): name of file to parse. Defaults to ....
			mode (literal, optional): reading mode. Defaults to 'r'.

		Returns:
			Any: parsed file
		"""
		with open(filename, mode) as file:
			return file.read(file)
