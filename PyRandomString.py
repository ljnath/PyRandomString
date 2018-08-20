from enum import Enum
import random
 
'''
Enum for selecting the type of random string
'''
class RandomStringType(Enum):
    __ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    NUMERIC = '0123456789'
    ALPHABET_LOWERCASE = __ALPHABET.lower()
    ALPHABET_UPPERCASE = __ALPHABET.upper()
    ALPHABET_ALL_CASE = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE
    ALPHA_NUMERIC_LOWERCASE = ALPHABET_LOWERCASE + NUMERIC
    ALPHA_NUMERIC_UPPERCASE = ALPHABET_UPPERCASE + NUMERIC
    ALPHA_NUMERIC_ALL_CASE = ALPHABET_ALL_CASE + NUMERIC
 
'''
Actual class containing methods to generate random strings
'''
class RandomString(object):
    def __init__(self):
        pass
 
    def get_strings(self, total_strings = 10, max_length = 10, random_length = False, randomStringType = RandomStringType.ALPHA_NUMERIC_ALL_CASE):
        string_collection = []
        if total_strings > 0 and max_length > 0:
            string_collection =  list(self.__get_strings(total_strings, max_length, random_length, randomStringType))
        return string_collection
 
    def __get_strings(self, total_strings, max_length, random_length, input_characters):
        for _ in range(total_strings):
            current_word = ''
            if not random_length:
                for _ in range(max_length):
                    current_word += random.SystemRandom().choice(input_characters.value)
            else:
                for _ in range(random.randint(1, max_length)):
                    current_word += random.SystemRandom().choice(input_characters.value)
            yield(str(current_word))
 

if __name__ == '__main__':
    randomString = RandomString()
    print(randomString.get_strings(5, 10, False, RandomStringType.ALPHABET_UPPERCASE))