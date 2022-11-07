# Python Binary Search
# By Aiden C for Comp Sci 2022
# Turns out the first time I wrote this code it was entirely broken, so I re-wrote it and here you go

# ----------
import time
import random

# Create a sorted array with arrlen items
arr = [0]
arrlen = 1000
while len(arr) < arrlen:
    arr.append(random.randrange(arr[len(arr) - 1] + 1, arr[len(arr) - 1] + 10))

# Define Variables
maximum = len(arr)
minimum = 0
found = False
searched = []

# Try because honestly somebody can probably find a way to break this
try:
    # Ask for input and handle errors
    print()
    number = input("Please enter a number: ")
    while not str.isdigit(number):
        number = (input("Please enter a number (not a string):"))
    number = int(number)

    # Advanced mode
    advanced = input("Would you like to enable advanced logging mode? (Y/N): ")

    # Print entire array for user
    print("\n- Searching array: " + str(arr))

    # Find index of input
    while not found:
        # Check to see if the program is in a loop and call error not found
        if minimum + int(((maximum - minimum) / 2)) in searched:
            found = True
            minimum = "Error"
            maximum = "Error"
            break

        # Record results and print if advanced mode
        searched.append(minimum + int(((maximum - minimum) / 2)))
        if advanced == "Y":
            time.sleep(1)
            print("Search log: Searching index range " + str(minimum) + " to " + str(
                maximum) + " with median value " + str(
                minimum + int(((maximum - minimum) / 2))) + "...")

        # Check for number successfully dialed-into
        if number == arr[minimum + int(((maximum - minimum) / 2))]:
            found = True

        # If not dialed-into change search parameters
        elif number > arr[minimum + int(((maximum - minimum) / 2))]:
            minimum = minimum + int(((maximum - minimum) / 2))
        elif number < arr[minimum + int(((maximum - minimum) / 2))]:
            maximum = minimum + int(((maximum - minimum) / 2))

    # Print Result
    if advanced != "Y":
        print("- Binary searching for your number at indexes: " + str(searched))

    if minimum == "Error":
        if number > arr[len(arr) - 1]:
            print("- Your number, " + str(number) + ", is greater then the array's largest value of " + str(
                arr[len(arr) - 1]) + ".")
        else:
            print("- Could not find " + str(number) + " in array.")
    else:
        print("- Found " + str(number) + " at index " + str(minimum + int(((maximum - minimum) / 2))) + "!")

# True error handling at it's finest
except:
    print("How in the world did you cause an error in my program...")
    print("Please report this")
