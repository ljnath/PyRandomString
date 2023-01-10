"""
MIT License

Copyright (c) 2023 Lakhya Jyoti Nath (ljnath)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

PyRandomString is a python library to generate N random list of string of M length
Version: 0.0.6
Author: Lakhya Jyoti Nath (ljnath)
Email:  ljnath@ljnath.com
Website: https://www.ljnath.com
"""

import sys

if sys.version_info[0] < 3:
    raise Exception("Python version lower than 3 is not supported")

import random
import re
from enum import Enum


class StringType(Enum):
    """
    Enum for selecting the type of random string
    """
    __ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    NUMERIC = '0123456789'
    SYMBOLS = '" !#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    ALPHABET_LOWERCASE = __ALPHABET.lower()
    ALPHABET_UPPERCASE = __ALPHABET.upper()
    ALPHABET_ALL_CASE = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE

    ALPHABET_LOWERCASE_WITH_SYMBOLS = __ALPHABET.lower() + SYMBOLS
    ALPHABET_UPPERCASE_WITH_SYMBOLS = __ALPHABET.upper() + SYMBOLS
    ALPHABET_ALL_CASE_WITH_SYMBOLS = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE + SYMBOLS

    ALPHA_NUMERIC_LOWERCASE = ALPHABET_LOWERCASE + NUMERIC
    ALPHA_NUMERIC_UPPERCASE = ALPHABET_UPPERCASE + NUMERIC
    ALPHA_NUMERIC_ALL_CASE = ALPHABET_ALL_CASE + NUMERIC

    ALPHA_NUMERIC_LOWERCASE_WITH_SYMBOLS = ALPHABET_LOWERCASE + NUMERIC + SYMBOLS
    ALPHA_NUMERIC_UPPERCASE_WITH_SYMBOLS = ALPHABET_UPPERCASE + NUMERIC + SYMBOLS
    ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS = ALPHABET_ALL_CASE + NUMERIC + SYMBOLS


class UnsupportedTypeException(Exception):
    """
    Exception class for UnsupportedTypeException. It is supposed to be raised if parameter is not of expected type
    """

    def __init__(self, parameter_name: str, message: str = None):
        print('Unsupported type exception for {}. {}'.format(parameter_name, message if message else ""))


class InvalidInputSymbolsException(Exception):
    """
    Exception class for InvalidInputSymbolsException. It is supposed to be when the custom symbol is not a subset of pre-defined symbols
    """

    def __init__(self, input_symbols: str):
        print('Input symbols "{}" are invalid. Input symbols should be a subset of available symbols {}'.format(input_symbols, StringType.SYMBOLS.value))


class RandomString():
    """
    Actual class containing methods to generate random strings
    """

    def __init__(self):
        pass

    def get_string(self, max_length: int = 10, random_length: bool = False, string_type: str = StringType.ALPHA_NUMERIC_ALL_CASE, symbols: str = None, must_include_all_type: bool = False):
        """ Generate a random string based on the input parameters.

        :param max_length: Maximum length of each generated string (default is 10).
        :param random_length: If True, the length of each word will be randomly chosen up to the maximum value (default is False).
        :param string_type: Type of characters to use for generating the strings.
        :param symbols: Custom symbols to use for generating the strings (applicable only when string_type is set to SYMBOLS or WITH_SYMBOLS).
        :param must_include_all_type: If True, characters from each type will be used in each generated string.
        :return: A random strings.
        """
        self.__validate_input(1, max_length, random_length, string_type, symbols)
        return self.get_strings(count=1,
                                max_length=max_length,
                                random_length=random_length,
                                string_type=string_type,
                                symbols=symbols,
                                must_include_all_type=must_include_all_type
                                )[0] if max_length > 0 else ''

    def get_strings(self, count: int = 10, max_length: int = 10, random_length: bool = False, string_type: str = StringType.ALPHA_NUMERIC_ALL_CASE, symbols: str = None, must_include_all_type: bool = False) -> list:
        """ Generate a list of random strings based on the input parameters.

        :param count: Total number of strings to generate (default is 10).
        :param max_length: Maximum length of each generated string (default is 10).
        :param random_length: If True, the length of each word will be randomly chosen up to the maximum value (default is False).
        :param string_type: Type of characters to use for generating the strings.
        :param symbols: Custom symbols to use for generating the strings (applicable only when string_type is set to SYMBOLS or WITH_SYMBOLS).
        :param must_include_all_type: If True, characters from each type will be used in each generated string.
        :return: A list of random strings.
        """
        self.__validate_input(count, max_length, random_length, string_type, symbols)
        list_of_strings = []
        if count > 0 and max_length > 0:
            list_of_input_strings = self.__get_input_strings_from_string_type(string_type)

            if symbols:
                # checking if user have specified any custom symbols, then the default symbols will be overridden
                list_of_input_strings = [symbols if '@' in entry else entry for entry in list_of_input_strings]

            input_characters = list_of_input_strings if must_include_all_type else ''.join(list_of_input_strings)
            list_of_strings = self.__get_strings(count, max_length, random_length, input_characters)
        return list_of_strings

    def __get_strings(self, count: int, max_length: int, random_length: bool, input_characters) -> list:
        """
        Generate a list of random strings from a single string of characters.

        :param count: Total number of strings to generate.
        :param max_length: Maximum length of each generated string.
        :param random_length: If True, the length of each word will be randomly chosen up to the maximum value.
        :param input_characters: String of characters or a list of strings of character to use for generating the strings.
        :return: A list of random strings.
        """
        strings = []
        if isinstance(input_characters, str):
            for _ in range(count):
                current_word = ''
                length = max_length if not random_length else random.randint(1, max_length)
                for _ in range(length):
                    current_word += random.SystemRandom().choice(input_characters)
                strings.append(str(current_word))
        elif isinstance(input_characters, list):
            for _ in range(count):
                current_word = ''
                length = max_length if not random_length else random.randint(1, max_length)
                for _ in range(length):
                    random_character_set = random.choice(input_characters)
                    current_word += random.SystemRandom().choice(random_character_set)
                strings.append(str(current_word))
        return strings

    def __validate_input(self, count: int, max_length: int, random_length: bool, string_type: StringType, symbols: str):
        """
        Validate the input parameters for correctness and compatibility.

        :param count: Total number of strings to generate.
        :param max_length: Maximum length of each generated string.
        :param random_length: If True, the length of each word will be randomly chosen up to the maximum value.
        :param string_type: Type of characters to use for generating the strings.
        :param symbols: Custom symbols to use for generating the strings (applicable only when string_type is set to SYMBOLS or WITH_SYMBOLS).
        """
        if not isinstance(count, int):
            raise UnsupportedTypeException('count', 'count should be of integer type instead of current {} type'.format(type(count)))

        if not isinstance(max_length, int):
            raise UnsupportedTypeException('max_length', 'max_length should be of integer type instead of current {} type'.format(type(max_length)))

        if not isinstance(random_length, bool):
            raise UnsupportedTypeException('random_length', 'random_length should be of boolean type instead of current {} type'.format(type(random_length)))

        if not isinstance(string_type, StringType):
            raise UnsupportedTypeException('string_type', 'string_type should be of StringType type instead of current {} type'.format(type(string_type)))

        if symbols and not isinstance(symbols, str):
            raise UnsupportedTypeException('symbols', 'symbols should be either None or of string type instead of current {} type'.format(type(symbols)))

        if symbols and not re.match('[{}]'.format(StringType.SYMBOLS.value), symbols):
            raise InvalidInputSymbolsException(symbols)

    def __get_input_strings_from_string_type(self, string_type: StringType) -> list:
        """
        Get a list of characters based on input string_type
        """
        strings = []
        if string_type == StringType.ALPHABET_LOWERCASE:
            strings = [StringType.ALPHABET_LOWERCASE.value]
        elif string_type == StringType.ALPHABET_UPPERCASE:
            strings = [StringType.ALPHABET_UPPERCASE.value]
        elif string_type == StringType.ALPHABET_ALL_CASE:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.ALPHABET_UPPERCASE.value]
        elif string_type == StringType.ALPHABET_LOWERCASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.SYMBOLS.value]
        elif string_type == StringType.ALPHABET_UPPERCASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_UPPERCASE.value, StringType.SYMBOLS.value]
        elif string_type == StringType.ALPHABET_ALL_CASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.ALPHABET_UPPERCASE.value, StringType.SYMBOLS.value]
        elif string_type == StringType.ALPHA_NUMERIC_LOWERCASE:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.NUMERIC.value]
        elif string_type == StringType.ALPHA_NUMERIC_UPPERCASE:
            strings = [StringType.ALPHABET_UPPERCASE.value, StringType.NUMERIC.value]
        elif string_type == StringType.ALPHA_NUMERIC_ALL_CASE:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.ALPHABET_UPPERCASE.value, StringType.NUMERIC.value]
        elif string_type == StringType.ALPHA_NUMERIC_LOWERCASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.NUMERIC.value, StringType.SYMBOLS.value]
        elif string_type == StringType.ALPHA_NUMERIC_UPPERCASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_UPPERCASE.value, StringType.NUMERIC.value, StringType.SYMBOLS.value]
        elif string_type == StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS:
            strings = [StringType.ALPHABET_LOWERCASE.value, StringType.ALPHABET_UPPERCASE.value, StringType.NUMERIC.value, StringType.SYMBOLS.value]
        return strings
