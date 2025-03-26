# Task 1: Positive or Negative Numbers
# Write a program that will let the user know if the number they
# have entered is positive or negative.

# 1. Ask the user to input a number
# 2. Using an 'if' statement, check if the number is greater than 0
#         If it is, print "{number} is positive."
# 3. Use an 'else' statement for when the number is not greater than 0.
#         In this case, print "{number} is negative."

# num = input("Choose a number.")
# if int(num) > 0:
#     print("Positive")
# else:
#     print("Negative")

    
# Task 2: Random Number Guesser III
# Create a Random Number Guesser program

# 1. Generate a random integer between 1 to 10
# 2. Ask the user to guess a number
# 3. If the user guesses correctly:
#     print "Congratulations!! You did it!"
# 4. If the user guesses wrongly: 
#     print "Oops, better luck next time!"

import random
ran = random.randint(1, 10)
num = input("Choose a number between 1-10")
if int(num) += ran:
    print("Cogratulations! You did it!")