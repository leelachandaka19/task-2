# Simple Calculator in Python

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

while True:
    # Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter operation (+, -, *, /): ")

    # Calculation 
    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        if num2 != 0:
            print("Result:", divide(num1, num2))
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
