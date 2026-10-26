#with slicing
s=input("Enter string:")
if s==s[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")

#without slicing
s1=input("Enter string:")
rev=""
for ch in s1:
    rev=ch+rev
if s1==rev:
    print("palindrome")
else:
    print("Not a palindrome")