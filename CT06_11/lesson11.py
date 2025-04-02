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

