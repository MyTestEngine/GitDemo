# s[i:j] - slice of s from i to j
# s[i:j:k] - slice of s from i to j with step k
# s[startindex:endindex:step]

s = "welcome to hello world of wonderful nature"
print(s[:])
print(s[0:])
print(s)
print(s[0:5])
print(s[-1:5])
print(s[-1])
print(s[4:10:2])
print(s[-1:])
print("This should print nature: ", s[-6:])
print("This should print wonderful:", s[-16:-7])
print("This should reverse the string: ", s[::-1])  # To reverse the string.

y = "name, age, city"
print(y.index(","))
print(y[0:y.index(",")])




