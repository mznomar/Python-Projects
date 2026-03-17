# -------------------------------------------------------------
# Program: For Loop Triangle Generator
# Course: COP1000
# Author: Omar Monzon
#Professor Dennis Hunchuck
#
# Description:
# This program asks the user to enter a number between 1 and 50
# and a character. The program validates the number and then
# generates two triangles:
# 1. A right triangle
# 2. An upside-down right triangle
# The program ends by printing "Thank You Hero!"
# -------------------------------------------------------------

def main():

    # Prompt the user for a number between 1 and 50
    number = int(input("Enter a number between 1 and 50: "))

    # Validate the number
    while number < 1 or number > 50:
        print("Invalid number. Please try again.")
        number = int(input("Enter a number between 1 and 50: "))

    # Prompt the user to enter a character
    character = input("Enter a character from the keyboard: ")

    print()

    # Generate the right triangle
    for row in range(1, number + 1):
        for col in range(row):
            print(character, end="")
        print()

    print()

    # Generate the upside down triangle
    for row in range(number, 0, -1):
        for col in range(row):
            print(character, end="")
        print()

    print()
    print("Thank You Hero!")


# Call to the main function
main()