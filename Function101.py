"""
Author: Omar Monzon
Professor: Dennis Hunchuck 
COP1000
Function 101

This program intents to demonstrate the different uses of functions
in Python. It starts asking the user for a name, counts the number
of letters in the name, displays the name that many times, and then
shows mathematical calculations based on the letter count.
"""

import math

def get_name():
    name = input("Please enter your name: ")
    return name

def name_counter(name):
    count = len(name)

    print("\nName:", name)
    print("Letter count:", count)

    for i in range(count):
        print(name)

    return count

def math_results(count):

    print("\nCount:",count)
    print("Square:", count ** 2)
    print("Cube:", count ** 3)

    root = math.sqrt(count)

    print("Square Root:", format(root, ".3f"))

def main():

    user_name = get_name()
    letter_count = name_counter(user_name)
    math_results(letter_count)

main()

