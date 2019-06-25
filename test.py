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

    def testStringRandomLength(self):
        random_strings = self.__random_string_generator.get_strings(count=5, max_length=20, random_length=True, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        for string in random_strings:
            assert re.fullmatch(r'[a-zA-Z0-9]{1,20}', string)
            
    def testForSingleString(self):
        random_string = self.__random_string_generator.get_string(max_length=6, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        assert random_string and len(random_string) == 6

    def testForSingleStringWithNoMaxLength(self):
        random_string = self.__random_string_generator.get_string(max_length=0, random_length=False, string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE)
        assert not random_string

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

    def testForUnsupportedTypeException(self):
        with self.assertRaises(PyRandomString.UnsupportedTypeException):
            self.__random_string_generator.get_strings(count = '2')
        with self.assertRaises(PyRandomString.UnsupportedTypeException):
            self.__random_string_generator.get_string(max_length = 'bad-input')
        with self.assertRaises(PyRandomString.UnsupportedTypeException):
            self.__random_string_generator.get_strings(random_length = 12345)
        with self.assertRaises(PyRandomString.UnsupportedTypeException):
            self.__random_string_generator.get_strings(string_type = 36.69)
        with self.assertRaises(PyRandomString.UnsupportedTypeException):
            self.__random_string_generator.get_strings(symbols = 321456)

    def testForInvalidInputSymbolsException(self):
        with self.assertRaises(PyRandomString.InvalidInputSymbolsException):
            self.__random_string_generator.get_strings(symbols='bad')

if __name__ == '__main__':
    unittest.main()
