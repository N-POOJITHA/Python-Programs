def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

n = int(input("Enter your choice: "))

a = int(input("Enter a: "))
b = int(input("Enter b: "))

match n:
    case 1:
        print("Result:", add(a, b))
    case 2:
        print("Result:", subtract(a, b))
    case 3:
        print("Result:", multiplication(a, b))
    case 4:
        print("Result:", division(a, b))
    case _:
        print("Invalid choice")