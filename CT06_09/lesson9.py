# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()'
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'

# import random
# x = random.randint(1, 6)
# y = random.randint(1, 6)
# z = random.randint(1, 6)
# print("1st number:" + str(x))
# print("2nd number:" + str(y))
# print("3rd number:" + str(z))
# b = 0
# b = b + (x) % 2
# b = b + (y) % 2
# b = b + (z) % 2
# c = b == 0 or b == 3
# print("All numbers are even/odd is " + str(c))

# Teacher solution
# import random
# num1, num2, num3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)
# print("1st number: " + str(num1))
# print("2nd number: " + str(num2))
# print("3rd number: " + str(num3))
# all_even_odd = (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0) or (num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1)
# print("All numbers are even/odd is " + str(all_even_odd))

# Task 6: Flowchart for Temperature Monitor
# You are analyzing daily temperature readings over a week.
# Write a program to count how many days had a temperature
# that is greater than 30.

# Draw out the flowchart (on a piece of paper) of the above
# program.

# 1. Start with creating and assigning the variable
#    "positive_days" to 0 before the loop.
# 2. Use a for loop to iterate through each day of the week
#    (7 times)
# 3. In each iteration the loop, prompt the user to input the
#    temperature for the day.
# 4. Use an 'if' condition to check if the temperature is greater
#    than 30. If so, increase the variable 'positive_days' by
#    1
# 5. After the loop, print the count of days with temperature
#    higher than 30.

# Task 8: Summing Positive Numbers
# **Task 8a**:
# Draw out the flowchart (on a piece of paper) of a program
# that will calculate the total sum of **savings** 
# (include in total only if savings for that day is positive)
# from a week's worth of data provided by the user every day.

# 1. Create and assign 'sum' variable to 0.
# 2. Use a 'for' loop to iterate through each day of the week
#    (7 times)
# 3. In each iteration, prompt the user to input the
#    savings for the day.
# 4. Use an if condition to check if the savings is greater
#    than 0. If so, increase the variable 'sum' by
#    that day's savings.
# 5. After the loop, print the sum of savings for that week

savings = 0
for i in range(7):
    savings = savings + input("What is your savings for today?")