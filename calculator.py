import math


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


# Percentage
def percentage(a, b):
    return (a / 100) * b


# Square
def square(a):
    return a * a


# Square root
def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of a negative number."
    return math.sqrt(a)


# Main calculator
def calculator():

    while True:

        print("\n========== PYTHON CALCULATOR ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Square")
        print("7. Square Root")
        print("8. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-8): ")

        # Exit
        if choice == "8":
            print("Thank you for using the calculator!")
            break

        # Check whether choice is valid
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please select a number from 1 to 8.")
            continue

        try:

            # Operations requiring two numbers
            if choice in ["1", "2", "3", "4", "5"]:

                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == "1":
                    result = add(a, b)

                elif choice == "2":
                    result = subtract(a, b)

                elif choice == "3":
                    result = multiply(a, b)

                elif choice == "4":
                    result = divide(a, b)

                elif choice == "5":
                    result = percentage(a, b)

            # Square
            elif choice == "6":

                a = float(input("Enter a number: "))
                result = square(a)

            # Square root
            elif choice == "7":

                a = float(input("Enter a number: "))
                result = square_root(a)

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numbers only.")


# Run the calculator
calculator()
