# Lesson 11 - AND OR NOT

# Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:

# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"

# px = input("Cost of your item?")
# if int(px) <= 5:
#     print("Sounds good!")
# elif int(px) <= 50:
#     print("Are you sure you need this?")
# elif int(px) <= 500:
#     print("Where are you getting this money from?!")
# else : 
#     print("Don't even think about it!")

# Task 1: AND Operator in Simple Conditions (AND)
# You are writing a program for an amusement park that needs to check
# if both riders of a ride are above the height of 120cm. Use the 'and'
# operator to determine if value of both 'rider1' and 'rider2' are
# greater than 120.

# rider1 = 125
# rider2 = 150
# >> True

# rider1 = 125
# rider2 = 150
# print(rider1 > 120 and rider2 > 120)

# Task 2: Multiples of 3 and 7 (AND)
# Create a program to check if a number is both divisible by 3 and 7

# 1. Ask the user to input a number
# 2. If the number is both a multiple of 3 and a multiple of 7:
#     print "The number is divisible by 3 and 7!"

# if num % 3 == 0 and num % 7 == 0:
#     print("True")
# else:
#     print("False")


# Task 4: 'or' Operator in Conditional Statements (OR)
# You run a go-kart business and need a program to check if at least
# 1 occupant of a 2-person go-kart is at least 18 years old.

# Use the 'or' operator to determine if value of either 'rider1' or
# 'rider2' is equal to or greater than 18.

# rider1 = 25
# rider2 = 6
# >> True

# rider1 = 25
# rider2 = 6
# if rider1 >= 18 or rider2 >= 18:
#     print("True")

# Task 5: Ticket Pricing Machine (OR)
# Create a program that will decide on the price of a ticket based on
# user's age. Original ticket price costs $20 per person. However,
# children below the age of 12 and elderly above the age of 65 can buy
# the ticket for just $15.

# 1. Ask user for their age
# 2. Use the 'or' operator to determine if user's age is less than 12 or
#    more than 65. If true, print "Ticket price: $15"
# 3. Else, print "Ticket price: $20"

# age = int(input("Age."))
# if age < 12 or age > 65:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20")


# Task 7: Colour filter (NOT)
# Create a program that will ask the user for a colour and print
# "Try again" if the input of the user is not "Green".

# 1. Ask user for a colour
# 2. Using the 'not' operator, check if input is not "Green".
#    If true, print "Try again"

# colour = input("Choose a colour.")
# if not (colour =="green"):
#     print("Try again.")

# Task 9: Not the Correct Password (NOT)
# Create a program that prompts for a password. If the entered password
# is not "Python123", the program should display "Access Denied."

# 1. Prompt the user for a password.
# 2. Using the 'not' operator, check if the password is not "Python123".
# 3. If true, display "Access Denied."

# password = "pw123"
# passs = input("Password.")
# if not (passs == password):
#     print("Äccess denied")

# Task 11: Login Credentials (AND, OR)
# Create a program that allows John to log in to TokTik.

# 1. John's username is 'John123' and his password is 'pw123'
# 2. The TokTik program will only allow John to log in.
# 3. Create 2 variables to store John's username and password
# 4. Ask John to enter his username and password
# 5. If both the username and password matches:
#     print "Access Granted"
# 6. If either the username or password is correct:
#     print "Either username or password is incorrect"
# 7. Otherwise:
#     print "Access Denied" 
# user = "John123"
# password = "pw123"
# use = input("What is your username? ")
# passs = input("WHat is YOur PaSSwOrd ")
# if user == use and password == passs :
#     print("Access Granted")
# elif user == use or password == passs:
#     print("Either username or password is incorrect")
# else:
#     print("Access denied")

# Task 12: Game status report (OR, NOT)
# Imagine you're programming a simple game. Write a conditional
# statement that checks whether a variable 'game_status' is either
# "active" or not "paused". Depending on the condition, print
# appropriate messages: "Game in progress..." or "Game is paused or
# inactive."

# 1. Declare a variable game_status and assign it a value
#    (e.g. "active").
# 2. Use an 'if' statement to check if 'game_status' equals "active"
#    OR if it's NOT equal to "paused" using the 'or' and 'not'
#    logical operator.
# 3. If the condition is 'True', print "Game in progress...".
# 4. Otherwise, print "Game is paused or inactive."