# len(s): Return the number of items in an object, If object is string it will return
# str() : converts specified value into a string
# upper(): converts a string into upper case
# count(sub[, start[, end]) : returns the number of times a specified value is found in the string
# isupper(): returns True if all characters are in the string are upper case
# islower(): returns True if all characters are in the string are lower case
# split(sep=None, maxsplit=-1) : Splits the string at the specified separator, and returns a value
# rsplit(): splits a string into a list, starting from the right.
# strip(): Returns a trimmed version of the string
# lstrip([chars]): Removes any leading characters
# rstrip([chars]): Removes any trailing characters
# replace(old, new[, count]): Replaces a specified phrase with another specified phrase.
# find(sub[, start[, end]]) : Searches the string for a specified value and returns the position
# index(sub[, start[, end]]) : Searches the string for a specified value and returns the position

x = "    ';';';'90808 The apple is sweet apple is apple is    ;"
y = 9789879879
# print(len(x))
#
# print(str(y))
# # print(y.find("78"))   # this fail with error::: AttributeError: 'int' object has no attribute 'find'
# print(str(y).find("78"))
# print(str(y).find("79"))
# print(x.islower())
# print(x.isupper())
# print(x.upper())
# print(x.lower())
# print(x.count("apple", 9, 50))
# print(x.replace("apple", "bannana", 2))
# print(x.index("ap", 5, 30))
# print(x.split(sep=' ', maxsplit=8))
# print(x.split())
print(x.strip(";9 '"))
print(x.lstrip(" ; 9 \'"))
print(x.rstrip(" ; 9 \'"))
print(x.replace("app", "bannnn"))

