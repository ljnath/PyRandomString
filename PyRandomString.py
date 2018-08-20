from enum import Enum
import random
 
'''
Enum for selecting the type of random string
'''
class RandomStringType(Enum):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    NUMERIC = '0123456789'
    ALPHABET_LOWERCASE = ALPHABET.lower()
    ALPHABET_UPPERCASE = ALPHABET.upper()
    ALPHABET_CASE_SENSITIVE = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE
    ALPHA_NUMERIC = ALPHABET + NUMERIC
    ALPHA_NUMERIC_CASE_SENSITIVE = ALPHABET_CASE_SENSITIVE + NUMERIC
 
'''
Actual class containing methods to generate random strings
'''
class RandomString(object):
    def __init__(self):
        pass
 
    def get_strings(self, total_words = 10, max_length = 10, random_length = False, randomStringType = RandomStringType.ALPHABET):
        string_collection = []
        if total_words > 0 and max_length > 0:
            string_collection =  list(self.__get_strings(total_words, max_length, random_length, randomStringType))
        return string_collection
 
    def __get_strings(self, total_words, max_length, random_length, input_characters):
        for _ in range(total_words):
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