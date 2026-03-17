"""
COP1000 - Decision A Assignment
Name: Omar Monzon
Prof: Dennis Hunchuck

This program asks the user to enter an integer value.
The program determines whether the value is even or odd,
whether it is a multiple of 3, whether it is a number in the teens,
and outputs a color (RED, WHITE, or BLUE) based on the input value.
"""
def main():

    # ----- INPUT -----
    value = int(input("Enter an integer: "))

    print("\nThe integer inputted was:", value)
    print()

    # ----- EVEN OR ODD -----
    if value % 2 == 0:
        print(value, "is an even number.")
    else:
        print(value, "is an odd number.")

    # ----- MULTIPLE OF 3 -----
    if value % 3 == 0:
        print(value, "is a multiple of 3.")
    else:
        print(value, "is not a multiple of 3.")

    # ----- TEENS CHECK -----
    if 13 <= value <= 19:
        print(value, "is a number in the teens.")
    else:
        print(value, "is a number NOT in the teens.")

    # ----- COLOR LOGIC -----
    if value < 10:
        color = "RED"
    elif value >= 20:
        color = "BLUE"
    else:
        color = "WHITE"

    print("The color based on", value, "is", color + ".")


# ----- CALL MAIN -----
if __name__ == "__main__":
    main()


