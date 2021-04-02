# Arithmatic operators
# Assignment operators
# Comparission operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators   ----compares the binary digits & (and), | (or), ~ (not), ^ (Xor)


#Logical operators  ---and or ----combines two comparision operators to check true or false
# x = 10
# y = 4
# print(x == y and x > y)
# print(x == y or x > y)
# # print(x == y && x > y)
# # print(x == y || x > y)
#
# #Identity operators - helps you compare objects
# obj1 = ['Apple', 'bat']
# obj2 = ['Apple', 'bat']
# print(obj1 == obj2)    # == compares the content of an object
# print(obj1 is obj2)   # is/is not compares the object not the content
# print(obj1 is not obj2)

#Membership operators   --- in/not in ---checks whether the value is in the list or not and returns true/false
obj1 = ['Apple', 'bat']
obj2 = ['Apple', 'bat']
print("bat" in obj1)
print("bat" not in obj1)
