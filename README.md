# PyRandomString
### Version : 0.0.5

Author : Lakhya Jyoti Nath (ljnath)<br>
Date : June 2019<br>
Email : ljnath@ljnath.com<br>
Website : https://www.ljnath.com

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrandomstring)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyrandomstring)
![PyPI - Status](https://img.shields.io/pypi/status/pyrandomstring)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyrandomstring)
[![Build Status][travis-image]][travis-link]
[![Code Coverage][codecov-image]][codecov-link]
[![HitCount][hit-count-image]][hit-count-link]
[![PyPI Version][pypi-image]][pypi-link]
![License][license-image-mit]



## Introduction
PyRandomString is a python library to generate N random list of string of M length
It is parameterized to generate strings of random number and length which is returned as a list. It can be used to generate a large number of numbers, strings etc.

## Parameters
* **count** : *Integer - Total number of strings to be generated (default is 10). Not applicable for get_string() method*
* **max_length** : *Integer - Maximum length of each generated string (default is 10)*
* **random_length** : *Boolean choice - if the length of each word should be random or not. Incase of random length the maximum value is 'max_length'*
* **symbols** : *String - Custom symbols which you want to use during random string generation. It should be a subset of the supported symbols and it is applicable only when the 'string_type' is of type 'SYMBOLS' or '_WITH_SYMBOLS'*
* **string_type** : *PyRandomString.StringType - Type of characters to be used for generating random strings*
    * **NUMERIC** : *0123456789*
    * **SYMBOLS** : *" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHABET_LOWERCASE** : *abcdefghijklmnopqrstuvwxyz*
    * **ALPHABET_UPPERCASE** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ*
    * **ALPHABET_ALL_CASE** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*
    * **ALPHA_NUMERIC_LOWERCASE** : *abcdefghijklmnopqrstuvwxyz0123456789*
    * **ALPHA_NUMERIC_UPPERCASE** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*
    * **ALPHA_NUMERIC_ALL_CASE** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*
    * **ALPHABET_LOWERCASE_WITH_SYMBOLS** : *abcdefghijklmnopqrstuvwxyz" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHABET_UPPERCASE_WITH_SYMBOLS** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHABET_ALL_CASE_WITH_SYMBOLS** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHA_NUMERIC_LOWERCASE_WITH_SYMBOLS** : *abcdefghijklmnopqrstuvwxyz0123456789" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHA_NUMERIC_UPPERCASE_WITH_SYMBOLS** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    * **ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" !#$%&'()\*+,-./:;<=>?@[\]^_`{|}~*
    

## How to use

```
import PyRandomString

py_random_string = PyRandomString.RandomString()

## calling method to get a single random string
random_string = py_random_string.get_string(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE, random_length=False, max_length=10)
print('Single random string is {}'.format(random_string))

## calling method to get a single random string with custom symbols
random_string = py_random_string.get_string(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS, random_length=False, max_length=10, symbols='+-*#$%^&')
print('Single random string with custom symbol is {}'.format(random_string))

## calling method to get a list of random string
random_strings = py_random_string.get_strings(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE_WITH_SYMBOLS, random_length=False, max_length=10, count=5)
print('Following are the generated random strings \n{}'.format('\n'.join(random_strings)))

```


[travis-image]: https://img.shields.io/travis/ljnath/PyRandomString/master.svg
[travis-link]: https://travis-ci.org/ljnath/PyRandomString
[pypi-image]: https://img.shields.io/pypi/v/pyrandomstring.svg
[pypi-link]: https://pypi.org/project/pyrandomstring/
[license-image-mit]: https://img.shields.io/badge/license-MIT-orange.svg
[hit-count-image]: http://hits.dwyl.io/ljnath/pyrandomstring.svg
[hit-count-link]: http://hits.dwyl.io/ljnath/pyrandomstring
[snyk-image]: https://snyk.io//test/github/ljnath/PyRandomString/badge.svg?targetFile=requirements.txt
[snyk-link]: https://snyk.io//test/github/ljnath/PyRandomString?targetFile=requirements.txt
[codecov-image]: https://codecov.io/gh/ljnath/pyrandomstring/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/ljnath/PyRandomString
