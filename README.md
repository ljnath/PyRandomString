# PyRandomString

## Introduction
PyRandomString is a python library to generate a list of string. 
It is parameterized to generate strings of random number and length which is returned as a list. It can be used to generate a large number of numbers, strings etc.



## Parameters
* **string_count**      : *Integer - Total number of strings to be generated (default is 10)*
* **max_length**      : *Integer - Maximum length of each generated string (default is 10)*
* **random_length**    : *Boolean choice - if the length of each word should be random or not. Incase of random length the maximum value is 'max_length'*
* **string_type** : *PyRandomString.StringType - Type of characters to be used for generating random strings*
    * **ALPHABET_LOWERCASE** : *abcdefghijklmnopqrstuvwxyz*
    * **ALPHABET_UPPERCASE** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ*
    * **ALPHABET_ALL_CASE** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*
    * **NUMERIC** : *0123456789*
    * **ALPHA_NUMERIC_LOWERCASE** : *abcdefghijklmnopqrstuvwxyz0123456789*
    * **ALPHA_NUMERIC_UPPERCASE** : *ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*
    * **ALPHA_NUMERIC_ALL_CASE** : *abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*
    

## How to use

```
import PyRandomString

random_string = PyRandomString.RandomString()
string_collection = random_string.get_strings(string_type=PyRandomString.StringType.ALPHA_NUMERIC_ALL_CASE, random_length=False, max_length=10, string_count=1000)

for current_string in string_collection:
    print(current_string)
```
