import ast
from typing import Any, Dict, List, Tuple

import num2word


''' for miscellaneous functions '''

class StringFormatting:

    def numToWord(num: int = ...) -> str:
        """Converts an integer to its corresponding word-phrase, i.e., 23 -> 'twenty three'

        Args:
            num (int, optional): number you want to convert. Defaults to ....

        Returns:
            str: corresponding word-phrase
        """
        return num2word.word(num).lower()

    def format_long(string: str = ..., cut: float = 0.50) -> str:
        """Reformats long strings based on 'cut' percentage and replaces former half with an ellipse.

        Args:
            string (str, optional): string you want to modify. Defaults to ....
            cut (float, optional): percentage of the first half of the string you want to reduce. Defaults to 0.50.

        Returns:
            str: formatted string
        """
        return '...{}'.format(string[round(len(string)*cut) :])

    def shorten(*cols, new_len: int = None) -> Tuple[Any]:
        """Returns a tuple of shortened columns. This was written for simple use with testing plotting functions

        Args:
            new_len (int, optional): new desired length. Defaults to None.

        Returns:
            tuple: tuple list of shortened data frames
        """
        return (col[:new_len] for col in cols)


class StringParsing:

    def parse_kwarg_string(kwargs_string: str = ...) -> Dict[str, Any]:
        """Parses a string of of kwargs (keyword arguments, e.g., "delim_whitespace=True, comment='#'") into a dictionary of the kwargs (particularly for use with a GUI). NOTE: Does not do well parsing strings that contain list substrings.

        Args:
            kwargs_string (str, optional): string containing keywords to parse. Defaults to ....

        Returns:
            dict: dictionary of parsed keyword arguments
        """
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


class ListCombining:

    def map_matrix(m: int = ..., n: int = ...) -> List[Tuple[int, int]]:
        """Creates a flattened list of matrix indexies (for subplots) for easy plotting.

        Args:
            m (int, optional): number of rows. Defaults to ....
            n (int, optional): number of columns. Defaults to ....

        Returns:
            A list of tuples representing the location of each subplot
        """
        return [(i+1, j+1) for i in range(m) for j in range(n)]

    # TODO - combine the three functions below into a single function
    def combine_to_tuple(primary_list: List[Any] = ..., secondary_list: List[Any] = ...) -> List[Tuple[Any, Any]]:
        """Combines to lists into a single lists with each corresponding item in one tuple.

        Args:
            primary_list (list, optional): first list to combine. Defaults to ....
            secondary_list (list, optional): second list to combine. Defaults to ....

        Returns:
            Combined lists as a single lists of tuples
        """
        assert len(primary_list) == len(secondary_list), "Lists must be of equal length"
        return [(i, j) for i, j in zip(primary_list, secondary_list)]

    def combine_to_dictionary(keys_list: List[Any] = ..., values_list: List[Any] = ...) -> Dict[Any, Any]:
        """Combines to lists into a single dictionary of key-value pairs. Both lists must be of the same length, and the list of keys must not contain any duplicates

        Args:
            keys_list (list, optional): list of assigned keys. Defaults to ....
            values_list (list, optional): list of corresponding values. Defaults to ....

        Returns:
            Dictionary of key-value pairs
        """
        assert len(keys_list) == len(values_list), "Lists must be of equal length"
        return {key: value for key, value in zip(keys_list, values_list)}

    def combine_list_strings(primary_list: List[Any] = ..., secondary_list: List[Any] = ...) -> List[str]:
        """Combines two strings into a single list of strings. Optional formats to be added.

        Args:
            primary_list (list, optional): primary list to combine. Defaults to ....
            secondary_list (list, optional): secondary list to combine. Defaults to ....

        Returns:
            List of strings combined from the two lists
        """
        assert len(primary_list) == len(secondary_list), "Lists must be of equal length"
        return ['{} ({})'.format(str(l1), str(l2)) for l1, l2 in zip(primary_list, secondary_list)]