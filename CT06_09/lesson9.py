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
c = b == 0 or b == 3
print("All numbers are even/odd is " + str(c))

# Teacher solution
# import random
# num1, num2, num3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)
# print("1st number: " + str(num1))
# print("2nd number: " + str(num2))
# print("3rd number: " + str(num3))
# all_even_odd = (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0) or (num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1)
# print("All numbers are even/odd is " + str(all_even_odd))