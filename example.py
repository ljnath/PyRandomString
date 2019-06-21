"""
Example implementation of the PyRandomString library
"""

import PyRandomString

py_random_string = PyRandomString.RandomString()

# calling method to get a single random string
random_string = py_random_string.get_string(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE, random_length=False, max_length=10)
print('Single random string is {}'.format(random_string))

# calling method to get a single random string with custom symbol
random_string = py_random_string.get_string(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS, random_length=False, max_length=10, symbols='+-*#$%^&')
print('Single random string with custom symbol is {}'.format(random_string))

# calling method to get a list of random string
random_strings = py_random_string.get_strings(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS, random_length=False, max_length=10, count=5)
print('Following are the generated random strings \n{}'.format('\n'.join(random_strings)))
