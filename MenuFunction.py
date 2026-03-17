"""
Author: Omar Monzon
Professor: Dennis Hunchuck
Course: COP1000
Assignment: Menu Function

Description:
This program demonstrates the use of functions and a menu system.
The user may enter numbers and then choose to display the current
sum, average, highest number, or lowest number. If the user tries
to display results before entering a number, the program will
advise the user to enter a number first.
"""


# Function to display the menu
def display_menu():
    print("\nMenu")
    print("G] Get a number")
    print("S] Display current sum")
    print("A] Display current average")
    print("H] Display the current highest number")
    print("L] Display the current lowest number")
    print("Q] Quit")


# Function to get the user's menu choice
def get_choice():
    choice = input("Enter your choice: ")
    return choice.upper()


# Function to get a number from the user
def get_number():
    number = float(input("Enter a number: "))
    return number


# Function to display the current sum
def display_sum(total, count):
    if count == 0:
        print("Please enter a number first.")
    else:
        print("Current sum:", total)


# Function to display the current average
def display_average(total, count):
    if count == 0:
        print("Please enter a number first.")
    else:
        average = total / count
        print("Current average:", format(average, ".3f"))


# Function to display the highest number
def display_highest(highest, count):
    if count == 0:
        print("Please enter a number first.")
    else:
        print("Current highest number:", highest)


# Function to display the lowest number
def display_lowest(lowest, count):
    if count == 0:
        print("Please enter a number first.")
    else:
        print("Current lowest number:", lowest)


# Main function
def main():

    # Initialize variables
    total = 0
    count = 0
    highest = 0
    lowest = 0
    choice = ""

    # Keep showing the menu until the user chooses Q
    while choice != "Q":
        display_menu()
        choice = get_choice()

        if choice == "G":
            number = get_number()
            total = total + number
            count = count + 1

            # First number entered becomes both highest and lowest
            if count == 1:
                highest = number
                lowest = number
            else:
                if number > highest:
                    highest = number
                if number < lowest:
                    lowest = number

        elif choice == "S":
            display_sum(total, count)

        elif choice == "A":
            display_average(total, count)

        elif choice == "H":
            display_highest(highest, count)

        elif choice == "L":
            display_lowest(lowest, count)

        elif choice == "Q":
            print("Goodbye")

        else:
            print("Invalid menu choice. Please try again.")


# Call the main function
main()