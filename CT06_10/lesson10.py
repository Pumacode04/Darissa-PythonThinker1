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

# import random
# ran = random.randint(1, 10)
# num = input("Choose a number between 1-10 ")
# IF int(num) == ran:
#     print("Cogratulations! You did it!")
# else:
#     print("Opps, better luck next time!")
    
# Task 3: Password Checker
# Code a password checker to protect your code!

# 1. Assign a password to a variable
# 2. Ask the user to enter a password
# 3. If the password matches, print "Login Successful"
# 4. If the password does not match, print "Password Incorrect"

# password = "passme"
# guess = input("What is the password? ")
# if guess == password:
#     print("Login successful!")
# else:
#     print("Password incorrect!")

# Task 4: Even or Odd?
# Code a program to tell the user if a number is even or odd

# 1. Ask the user to input a number
# 2. Using the '%' operator, find out if a number is divisible by 2
#    (A number that is divisible by 2 will leave no remainder when
#    divided by 2)
# 3. If the number is even, print "This number is even"
# 4. If the number is odd, print "This number is odd"

# num = input("Choose any number.")
# if int(num) % 2 == 1:
#      print("This number is odd")
# else:
#     print("This numvber is even")

# Task 5: Simple Age Checker (nested if..else)
# Using nested if..else condition, write a program that categorizes
# a person's age as 'Child', 'Teen', or 'Adult'.

# 1. Initialize an 'age' variable and ask user for their age.
# 2. Use an 'if' statement to check if the age is less than 13.
#         If true, print "Child"
# 3. Within the 'else' statement of the 1st 'if' statement, use
#    another 'if' statement to check if the age is between 13 and 19.
#         If true, print "Teen"
# 4. Else:
#         Print "Adult"

# age = int(input("How old are you?"))
# if age <= 12:
#      print("Child")
# else:
#      if age <= 19:
#         print("Teen")
#      else:
#         print("Adult")

# age = int(input("How old are you?"))
# if age <= 12:
#     print("Child")
# elif age <= 19:
#     print("Teen")
# else:
#     print("Adult")