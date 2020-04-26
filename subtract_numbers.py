"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
The user is expected to always enter valid real numbers as input.
Negative values are acceptable
This problem is a sandcastle!
"""


def main():
    print("This program subtracts one number from another.")
    print("User can enter valid real numbers as input.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = float(num1 - num2)
    print("The result is " + str(total) + ".")
    print(type(total))
    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
