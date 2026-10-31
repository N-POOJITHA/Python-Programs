list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for i in list1 + list2:
    if i not in result:
        result.append(i)

print(result)