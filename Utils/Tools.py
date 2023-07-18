import ast
from typing import Any, List, Tuple

import num2word

''' for miscellaneous functions '''

class Tools:
    
    def numToWord(num: int = ...) -> str:
        # as name suggest, returns word for a number
        return num2word.word(num).lower()

    def format_long(string: str = ..., cut: float = 0.50) -> str:
        # cuts off a string at desired point and adds ellipses
        return '...{}'.format(string[round(len(string)*cut) :])

    def shorten(*cols, new_len: int = None):
        # returns tuple of shortened lists/dataframes
        # this was written for simple use with testing plotting functions
        return (col[:new_len] for col in cols)
        
    def map_matrix(m, n):
        # returns  flattened list of subplot slots
        return [(i+1, j+1) for i in range(m) for j in range(n)]
    
    def combine_to_tuple(list1: List[Any] = ..., list2: List[Any] = ...):
        return [(i, j) for i, j in zip(list1, list2)]

    def combine_to_dictionary(list1: List[Any] = ..., list2: List[Any] = ...):
        return {key: value for key, value in zip(list1, list2)}
    
    def combine_list_strings(list1: List[Any] = ..., list2: List[Any] = ...):
        # combined two lists of strings into a single list
        return ['{} ({})'.format(str(l1), str(l2)) for l1, l2 in zip(list1, list2)]

    def parse_kwarg_string(kwargs_string: str = ...):
        # parses a str of kwargs (e.g., "delim_whitespace=True, comment='#'")
        # into a dictionary of the kwargs (particularly for use with a GUI)
        pairs = kwargs_string.split(',')
        arguments = [pair.split('=') for pair in pairs]
        kwargs_dict = {}
        for arg in arguments:
            keyword = arg[0].strip()
            value = arg[1].strip()
            try:
                value = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                value = value.strip("'")
            kwargs_dict[keyword] = value
        return kwargs_dict
