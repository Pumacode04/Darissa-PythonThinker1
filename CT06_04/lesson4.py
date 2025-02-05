# Lesson 4 - Strings

## Recap 1: Sushi Checkout

# You just had a lunch at a sushi restaurant and have to
# calculate the total amount you have spent. Different coloured
# plates costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates, and 4
# green plates.

# Calculate and print the total amount you have spent: -->

# Answer below
# Red = 1
# Blue = 2
# Green = 3
# Total = (Red) * 3 + (Blue) * 5 + (Green) * 4
# print(Total)

# for fun :

# Apple = "Red"
# print(Apple)

## Task 1: Storing and printing Strings

# **Task 1a**:
# Use the input() function to ask the user for their name and
# store it in a variable. Then print that variable.

# **Task 1b**:
# Ask the user for their favorite colour using input() and
# store the response in a variable. Print the variable.

# **Task 1c**:
# Ask the user for their age using input() and store the answer
# in a variable. Print the variable.

# You = input("Tell me your name.")
# print(You)

# Color = input("Tell me your favourite color")
# print(Color)

# Age = input("Tell me your age.")
# print(Age)



## Task 2: Input & string concatenation

# **Task 2a**:
# Ask the user for their name using input() and store it in a
# variable. 
# Concatenate the name with "Hi, [name]!" and print the
# complete message.

# **Task 2b**:
# Use input() to ask the user for their favorite hobby. Store this
# in a variable.
# Print a message saying "I enjoy [hobby]" using string
# concatenation.

# **Task 2c**:
# Ask the user for their dream vacation destination using input()
# and store it in a variable.
# Concatenate this variable with a phrase like "I would love to
# visit" and print the full sentence.

Name = input("Tell me your name.")
print("Hi," + (Name))

Hobby = input("Tell me your favourite hobby.")
print("I enjoy " + (Hobby))

DreamVacation = input("Tell me your dream vacation.")
print("Hi," + (DreamVacation))