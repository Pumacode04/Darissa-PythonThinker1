# Lesson 8 - Importing Libraries, Boolean & Conditions

## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
# product = 1
# for i in range(1, 6) :
#     number = input("What is number #" + str(i))
#     product = int(number) * product
# print(product)

## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.

# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# import time
# for i in range(int(input("Starting number.")), int(input("Ending number")) - 1, -1):
#     print(i)
#     time.sleep(1)

## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

# import random
# print(random.randint(2, 5))

# import random
# for i in range(20):
#     print(random.randint(1, 9998))


## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.

# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.

# Print out the result of comparing the 2 variables using
# the "==" operator.

# x = 5
# y = 6
# print(x == y)

# x = 2
# y = 2
# print(x == y)


## Task 4:

# **Task 4a**: Math Question Generator
# Using the 'random' library, generate 2 numbers between 1 and 50
# that the user must add together.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# Example:
# What is 2 + 5? << 7 >>
# True

# import random
# x = random.randint(2, 49)
# y = random.randint(2, 49)
# z = input("What is " + str(x) + " + " + str(y) + "?")
# print(int(z) == x + y)

# **Task 4b**: Range Guesser
# Create a program that generates a random number between 1 and
# 50.

# The user should input a range (two numbers: start and end).

# The program checks if the random number falls within the user's
# range.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# import random
# x = random.randint(2, 49)
# y = input("smaller number")
# z = input("bigger number")
# print(int(y) <= x <= int(z))
# or
# print(x <= z and x >= int(y)

## Task 5: Random Number Guessing Game

# Create a simple program to guess a random number:
# a. Create a variable called 'guess' and assign a number that
#    you are guessing
# b. Create a variable called 'num1' and assign a random integer
#    between 1 to 10.

# Your program will check if 'guess' is equal to 'num1'.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# import random
# guess = input("What is your guess? (the number is between 1 and 10)")
# num1 = random.randint(2, 9)
# print(guess == num1)


## Task 6: Random Multiplication Quiz

# You have been tasked by Ms Tan, the Math teacher to create a
# multiplication quiz.

# Create a program that generates a certain number of random
# multiplication questions.

# Each question should involve multiplying 2 random numbers
# between 1 and 10. The user should input the number of questions
# they want to attempt.

# import random
# Quest = input("How much questions you want to attempt?")
# for i in range(int(Quest)):
#     x = (random.randint(2, 10))
#     y = (random.randint(2, 10))
#     z = input("What is " + str(x) + " x " + str(y) + "?")
#     print(int(z) == y * x)

## Task 7: Even or Odd Checker

# Write a program that asks the user to enter a number. The
# program then tells the user whether the number is even
# (True) or odd (False).

# Your program needs to:
# 1. Ask user for an integer input.
# 2. Check if there is any remainder when user input is divided
#    by 2 (using '%').
# 3. Print 'True' if number is even, otherwise print 'False'.

# Key = input("Choose a number.")
# Hi = int(Key) % 2
# print(Hi == 0)

## Task 8: Multiple Check Program

# Create a program where the user enters 2 numbers. The
# program then checks if the first number is a multiple of
# the second number.

# Your program needs to:
# 1. Get user to input 2 numbers.
# 2. Check if there is any remainder when number #1 is divided
#    by number #2
# 3. Print 'True' if number #1 is a multiple of number #2,
#    otherwise print 'False'.

# BNum = input("Choose a number.")
# SNum = input("Choose a number that is smaller than the previous one.")
# Difference = int(BNum) % int(SNum)
# print(Difference == 0)