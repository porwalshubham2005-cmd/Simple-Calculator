"""
Codveda Technologies
Python Development Internship

Task 1: Simple Calculator

Description:
A basic calculator that performs four arithmetic operations:
Addition, Subtraction, Multiplication, and Division.
"""


"""
Codveda Technologies
Python Development Internship

Task 1: Simple Calculator

Description:
A basic calculator that performs four arithmetic operations:
Addition, Subtraction, Multiplication, and Division.
"""

def addition(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtraction(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiplication(a, b):
    """Return the product of two numbers."""
    return a * b

def division(a, b):
    """Return the division result and handle division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."

    return a / b

def display_menu():
    """Display calculator operation menu."""
    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


def main():
    """Run the Simple Calculator."""

    print("=" * 45)
    print("           SIMPLE CALCULATOR")
    print("=" * 45)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\nError: Please enter valid numbers.")
        return

    display_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = addition(num1, num2)

    elif choice == "2":
        result = subtraction(num1, num2)

    elif choice == "3":
        result = multiplication(num1, num2)

    elif choice == "4":
        result = division(num1, num2)

    else:
        result = "Invalid choice. Please select between 1 and 4."

    print("\n" + "=" * 45)
    print("Result:", result)
    print("=" * 45)

if __name__ == "__main__":
    main()