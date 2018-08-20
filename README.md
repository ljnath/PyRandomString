# PyRandomString

## Introduction
PyRandomString is a python library to generate a list of string. 
It is parameterized to generate strings of random number and length which is returned as a list.


## Parameters
* **total_words**      : *Integer - Total number of strings to be generated (default is 10)*
* **max_length**      : *Integer - Maximum length of each generated string (default is 10)*
* **random_length**    : *Boolean choice - if the length of each word should be random or not. Incase of random length the maximum value is 'max_length'*
* **randomStringType** : *RandomStringType - Type of characters to be used for generating random strings *
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

randomString = PyRandomString.RandomString()
string_collection = randomString.get_stings()
print(string_collection)
```
