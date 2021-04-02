# define two variables
x = "Python Class"
y = "ABC world of knowing"

print("Welcome to "+ x+" from "+ y)
# instead we can use % operator
print("Welcome to %s from %s" %(x, y))
print("Welcome to %s from %s" %("Python Class", y))

# Now let's  use format method which more efficient
print("Welcome to {} from {}".format(x, y))

# now this formatting can be done with indexing too
print("Welcome to {0} from {1}".format(x, y))  # is the most recommended format the string

#we can also use keyword argument as below
print("Welcome to {classname} from {schoolname}".format(classname=x, schoolname=y))   # is the more readable code

print("Welcome to {0} from {1} where we have {studentscount} in our place".format(x, y, studentscount = 100))
