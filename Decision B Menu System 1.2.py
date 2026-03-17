"""
Decision B - COP1000 Menu System
Author: Omar Monzon
Date: 03/01/2026
Description:
    A simple Python menu-driven program that can:
      1) Ask for a name and display it
      2) Ask for age and display a statement based on rules
      3) Display today's date in MM/DD/YYYY format
      4) Quit
"""

from datetime import datetime


def display_menu() -> None:
    """Display the main menu options."""
    print("\n*** MAIN MENU ***")
    print("1. Get a name then display the name")
    print("2. Get age then display statement")
    print("3. Today's date")
    print("4. Quit")


def option_get_name() -> None:
    """Option 1: Ask for a name and display a greeting."""
    name = input("What is your name: ").strip()
    print(f"\nHello {name}, have a good day.\n")


def option_get_age() -> None:
    """Option 2: Ask for age and display a statement based on rules."""
    try:
        age = int(input("How old are you: "))
    except ValueError:
        print("\nPlease enter a valid whole number.\n")
        return

    # Priority matters: age > 60 must be checked first
    if age > 60:
        print(f"\nWow, {age} is really old.\n")
    elif age >= 21:
        print(f"\nSince you are {age}, let's go have a drink.\n")
    elif age < 10:
        print(f"\nYou are only {age} go to bed.\n")
    else:
        # Ages like 19 produce no output (per assignment sample)
        print()


def option_show_date() -> None:
    """Option 3: Display today's date in MM/DD/YYYY format."""
    today = datetime.now().strftime("%m/%d/%Y")
    print(f"\nToday's date is {today}\n")


def main() -> None:
    """Main function controlling the menu loop."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            option_get_name()
        elif choice == "2":
            option_get_age()
        elif choice == "3":
            option_show_date()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")


# Required call to main function
if __name__ == "__main__":
    main()