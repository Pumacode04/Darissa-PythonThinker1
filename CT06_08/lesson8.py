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

import random
x = random.randint(2, 49)
y = random.randint(2, 49)
z = input("What is " + str(x) + str(y))
z == x * 