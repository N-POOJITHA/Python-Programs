numbers=[10,25,7,42,25,30]
largest=float('-inf')
second_largest=float('-inf')
for n in numbers:
    if n>largest:
        second_largest=largest
        largest=n
    elif n>second_largest and n!=largest:
        second_largest=n

print("Second Largest is:",second_largest)