
numbers = [0, 1, 0, 3, 12]
result = []

for num in numbers:
    if num != 0:
        result.append(num)

zeros = len(numbers) - len(result)

for i in range(zeros):
    result.append(0)

print(result)
