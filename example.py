"""
Example implementation of the PyRandomString library
"""

import PyRandomString

py_random_string = PyRandomString.RandomString()
string_collection = py_random_string.get_strings(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE, random_length=False, max_length=10, string_count=1000)

for current_string in string_collection:
    print(current_string)
