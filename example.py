import PyRandomString

randomString = PyRandomString.RandomString()
string_collection = randomString.get_strings(randomStringType=PyRandomString.RandomStringType.ALPHA_NUMERIC_ALL_CASE, random_length=True, max_length=2)
print(string_collection)