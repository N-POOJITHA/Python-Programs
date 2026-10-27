s=input("Enter string:" )
r=""
for ch in s:
    if ch not in r:
        r+=ch

print(r)