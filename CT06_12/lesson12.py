
# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25
# people = 50
# while people < 50 :
#     print(people)
#     people += 1
# print("The venue is done")
# people = input("How many people you want? ")
# maximum = input("How much people is the maximum? ")
# print("Vistors already present : " + people)
# print("Max visitors allowed : " + maximum)

# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.

people = 0
while True :
    if people == 30 :
        break
    else:
        people += 1
print("Visitors : " + int(people))