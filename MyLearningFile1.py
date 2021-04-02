# This is Learning file

a = 3
b, c, d = 5, 6.5, "Hello"
print("{} {}".format(d, c))   #printing string and int
print(type(a) , type(b), type(c), type(d))

#
values = [1, 2, "hello", 4, 5]   # lists are defined in square bracket


#print("The python list value of", {}.format(values[0]))
values.insert(3, "well")   # To insert value to the list

values.append("End")   # to insert a value at the end of list
values[2] = "HELLO"
del values[1]
print(values)

# define a tuple
tuplevalue = (1, 3, "abcd", 100, 145.05)
print ("Here is the tuple value   ", "{}  {}  {}  {}  {}".format(tuplevalue[0], tuplevalue[1], tuplevalue[2], tuplevalue[3], tuplevalue[4]))

#tuplevalue(3) = "ABCD"
print ("Here is the tuple value after the change   ", "{}  {}  {}  {}  {}".format(tuplevalue[0], tuplevalue[1], tuplevalue[2], tuplevalue[3], tuplevalue[4]))

# Dictionary
mybook = {"name":"A1", "author":"Apple1", "published_by":"prime printers", "bookcount": 10}
print("Here is my dictionary", mybook)
print(mybook["author"])
# print("bookname ", {}, "have count ", {}.format(mybook["name"], mybook["bookcount"]))   Receiving error as format cannot dictionary
#Create dictionary dynamically at runtime
myworld = {}
myworld["firstname"] = "Apple1"
myworld["lastname"] = "Cinnamon1"
myworld["gender"] = "Male"

print(myworld)

#Lesson 10: If else condition
greeting = "Good Morning"
a = 4
if greeting == "Good Morning":
    if a == 2:
        print("My count is 2")
    print("I am correct match")
else:
    print("Having wrong match")
print("If condition code is completed")

#Lesson 11: Loops in Python
# print array items in each line
obj = [100, 5, 3, 7, 10]

for i in obj:
    print(i)

print("sum of obj")

for j in obj:
     summation = j + summation
print(summation)


