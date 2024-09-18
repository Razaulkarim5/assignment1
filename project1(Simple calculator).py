
# 1. Addition
def add(x, y):
    return x + y

# 2. Subtraction
def subtract(x, y):
    return x - y

# 3. Multiplication
def multiply(x, y):
    return x * y

# 4. Division
def divide(x,y):
    try:
        if y != 0:
            return x / y
        else:
            raise ZeroDivisionError("Division by zero is not allowed.")
    except ZeroDivisionError as e:
        return str(e)
# 5. Modulus
def modulus(x, y):
    return x % y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    # Taking input from the user for operation choice
    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid choice! Please select a number between 1 and 5.")
    except ValueError as e:
        print(e)
        return
    # Taking input for the two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
  # Performing the chosen operation
    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        result = divide(num1, num2)
        print( f"{num1} / {num2} = {result}")
    elif choice == 5:
        print('Modulus: 'f"{num1} % {num2} = {modulus(num1, num2)}")

# Running the calculator
calculator()
