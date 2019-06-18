"""
PyRandomString test script
"""

import unittest
import re
import PyRandomString

class TestPyRandomString(unittest.TestCase):
    def setUp(self):
        self.__random_string_generator = PyRandomString.RandomString()

    def tearDown(self):
        pass

    def testStringCount(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=6, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        assert len(random_strings) == 5

    def testStringLength(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=8, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        for string in random_strings:
            assert len(string) == 8

    def testForAlphabetInUpperCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=10, random_length=False, string_type=PyRandomString.StringType.ALPHABET_UPPERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[A-Z]{10}', string)

    def testForAlphabetInLowerCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=12, random_length=False, string_type=PyRandomString.StringType.ALPHABET_LOWERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-z]{12}', string)

    def testForAlphabetInMixedCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=14, random_length=False, string_type=PyRandomString.StringType.ALPHABET_ALL_CASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z]{14}', string)

    def testForAlphaNumericInUpperCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=16, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_UPPERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9]{16}', string)

    def testForAlphaNumericInLowerCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=18, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_LOWERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9]{18}', string)

    def testForAlphaNumericInMixedCase(self):
        random_strings = self.__random_string_generator.get_strings(string_count=5, max_length=20, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9]{20}', string)


if __name__ == '__main__':
    unittest.main()
