item = [0, 0, 1, 1, 2, 2, 3, 4, 5, 5]

temp = []

for x in item:
    if x not in temp:
        temp.append(x)

print(len(temp))