import logging
import os
import time
import timeit
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Literal, Tuple, TypedDict, Union

# formatted date
today = datetime.now()
formatted_date = today.strftime("%Y_%B_%d")


''' Backend for implementation of logging for any Python program '''

class LoggerBackend:

	_instance = None
	def __new__(
			cls,
			log_file: str = ...,
			log_level: Callable = logging.DEBUG,
			format: Any = None,
			stream_handler_level: Callable = logging.INFO
   	):
		"""Backend logging configuration class object. Does not need to be independently instantiated, all methods are inherited by the child class.

		Args:
			log_file (str, optional): save name for log file. Defaults to ....
			log_level (Callable, optional): logging level configuration, defined by 'logging' library parameters. Defaults to logging.DEBUG.
			format (Any, optional): string format for log message. Defaults to None.
			stream_handler_level (Callable, optional): stream handler for simultaneous terminal printing (part of 'logging' library). Defaults to logging.INFO.
		"""

		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.logger = logging.getLogger(__name__)
			cls._instance.logger.setLevel(log_level)

			if format is None:
				formatter = logging.Formatter('[%(asctime)s :: %(levelname)-4s] %(message)-s')

			log_file = LoggerBackend.generate_unique_name(log_file)
			# Define the log file name and create a file handler
			file_handler = logging.FileHandler(log_file)
			file_handler.setLevel(log_level)
			file_handler.setFormatter(formatter)
			cls._instance.logger.addHandler(file_handler)

			# Create a stream handler to print log messages to the console
			stream_handler = logging.StreamHandler()
			stream_handler.setLevel(stream_handler_level)
			stream_handler.setFormatter(formatter)
			cls._instance.logger.addHandler(stream_handler)

		return cls._instance

	@staticmethod
	def generate_unique_name( 
		filename: str = ...,
		path: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__))), # CWD
		copy_pattern: str = 'Run'
		):
		"""Static function for producing updating enumeration of consecutive log files.

		Args:
			filename (str): original name of file. Defaults to ...
			path (str, optional): defualt directory for saving log files. Defaults to os.path.dirname(os.path.dirname(os.path.abspath(__file__))).
			copy_pattern (str): appended pattern. Defaults to "Run"

		Returns:
			str: filename with unique number identifier appended to original filename
		"""
		base_name, ext = os.path.splitext(filename)
		unique_name, counter = filename, 1
		while os.path.exists(os.path.join(path, unique_name)):
			counter += 1
			unique_name = f"{base_name} ({copy_pattern} {counter}){ext}"

		return unique_name


class Logger(LoggerBackend):

	def __init__(self, *args, **kwargs) :
		"""
  		Class object which includes log decorator for function logging with optional function timer
    		and option for manual logging, based on configuration executed in the parent class, LoggerBackend.
		"""
		super().__init__(*args, **kwargs)

	def log(
			self,
			message: str = None,
			message_type: Literal['debug', 'info', 'warning', 'error', 'critical'] = 'info',
			time_execution: bool = False
   		):
		"""Function decorator for automated logging, includes function timer, and option to log any combination of message and timer.

		Args:
			message (str, optional): message to log. Defaults to None.
			message_type (str, optional): type of message listed in 'logging' library. Defaults to 'info'.
			time_execution (bool, optional): option to time function exectuion and log results. Defaults to False.
		"""
		def decorator(func):
			@wraps(func)
			def wrapper(*args, **kwargs):
				function_name = func.__name__

				if message is not None:
					self.manual_log(message, message_type)

				if time_execution:
					start_time = timeit.default_timer()

				result = func(*args, **kwargs)
				if time_execution:
					elapsed_time = timeit.default_timer() - start_time

					self.manual_log(f"{function_name} executed in {elapsed_time:.6f} seconds", message_type)

				return result
			return wrapper
		return decorator

	def manual_log(
			self,
			message:str = ...,
			message_type: Literal['debug', 'info', 'warning', 'error', 'critical'] = 'info',
			*args,
   			**kwargs
		):
		"""Optional logging for manual messages.

		Args:
			message (str, optional): message to log. Defaults to ....
			message_type (str, optional): type of logging messaged listed in 'logging' library. Defaults to 'info'.
		"""
		if message in [None, 'none', 'None'] or 'None' in message:
			pass
		else:
			if message_type == 'debug':
				self.logger.debug(message, *args, **kwargs),
			elif message_type == 'info':
				self.logger.info(message, *args, **kwargs),
			elif message_type == 'warning':
				self.logger.warning(message, *args, **kwargs),
			elif message_type == 'error':
				self.logger.error(message, *args, **kwargs),
			elif message_type == 'critical':
				self.logger.critical(message, *args, **kwargs),
			else:
				pass


class LogDictConfig(TypedDict):
	""" Dictionary type hint configuration (currently unused). """
	filename: str
	filemode: Literal['w', 'a']
	format: str
	level: Callable