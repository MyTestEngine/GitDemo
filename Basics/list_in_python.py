# list.append(x)  -- Add an item to the end of list
# list.insert(i, x)  -- Insert an item at a given position
# list.remove(x) ---Remove the first item from the list whose value is equal to x
# list.pop([i])   ---Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes
# and returns the last item in the list

x = 10
y = "training"

z = [10, 20, 30, 40, 50, 60, "school"]
z1 = ['aaa', 'bbb', 'ccc']
print(z == z1)
i = 0
for i in range(len(z)):
    print(z[i])

z.append(50)   # append adds new index value at the end of list
print(z[-1:])
print(z[::-1])
z.insert(1,"fixme")
print(z)

