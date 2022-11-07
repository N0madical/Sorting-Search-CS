# Python Sequential Search
# By Aiden C for Comp Sci 2022
# I tried a different coding method using try and accept this time

# ----------

# Pre-start imports and definitions
import random
Found = False

# Create 1000-element array with numbers between 0 and 100
arr = []
for i in range(0, 1000):
    arr.append(random.randrange(0, 100))

# Ask user for input
number = input("\nPlease enter the number you like to search for: ")
while not str.isdigit(number):
    number = (input("Please enter a number (not a string):"))
number = int(number)

# Sequential search array
print("\nSequential searching array with " + str(len(arr)) + " terms: " + str(arr))
for i in range(0, len(arr)):
    if arr[i] == number:
        try:
            indexes = str(indexes) + ", " + str(i)
        except:
            indexes = i

# Print results
try:
    if type(indexes) == int:
        print("Found " + str(number) + " at index: " + str(indexes))
    else:
        print("Found " + str(number) + " at indexes: " + str(indexes))
except:
    print("Could not find " + str(number) + " in array.")
