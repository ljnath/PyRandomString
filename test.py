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

    def testStringLength(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=8, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        for string in random_strings:
            assert len(string) == 8

    def testForSingleString(self):
        random_string = self.__random_string_generator.get_string(max_length=6, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        assert random_string and len(random_string) == 6

    def testStringCount(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=6, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        assert len(random_strings) == 5
    
    def testForAlphabetInUpperCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=10, random_length=False, string_type=PyRandomString.StringType.ALPHABET_UPPERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[A-Z]{10}', string)

    def testForAlphabetInLowerCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=12, random_length=False, string_type=PyRandomString.StringType.ALPHABET_LOWERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-z]{12}', string)

    def testForAlphabetInMixedCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=14, random_length=False, string_type=PyRandomString.StringType.ALPHABET_ALL_CASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z]{14}', string)

    def testForAlphaNumericInUpperCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=16, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_UPPERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[0-9A-Z]{16}', string)

    def testForAlphaNumericInLowerCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=18, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_LOWERCASE)
        for string in random_strings:
            assert re.fullmatch(r'[0-9a-z]{18}', string)

    def testForAlphaNumericInMixedCase(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=20, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9]{20}', string)

    def testForAlphaNumericInMixedCaseWithSymbols(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=22, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9" !"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]{22}', string)

    def testForAlphaNumericInMixedCaseWithCustomSymbols(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=24, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS, symbols='*&^%$#@!+-=')
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9*&^%$#@!+-=]{24}', string)

if __name__ == '__main__':
    unittest.main()
