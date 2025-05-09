# Task 1: List of groceries
# **Task 1a**:
# Create a list of 8 groceries you need to buy:
# 1. Apples
# 2. Bread
# 3. Carrots
# 4. Dates
# 5. Eggs
# 6. Flour
# 7. Grapes
# 8. Honey

# food = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Honey"]
# food[7] = "Herbs"
# food.append("Ice")
# food.insert(1, "Bananas")
# food.pop(2)
# OR
# del(food[2])
# print(food)

# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"

# foods = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Honey"]
# for food in foods:
#     if foods == "Apples":
#         print(foods) + ": I need 5 of these")
#     elif foods == "Carrots":
#         print(foods) + ": I need 3 of these")
#     elif foods == "Grapes":
#         print(foods) + ": Get the FarmFresh brand")
#     else:
#         print(foods)

# basket = []
# while True:
#     food = input("What do you want to add?")
#     if food != "end":
#         basket.append(food)
#     else:
#         break
# for food in basket:
#     print("I have bought " + food)

# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."

# store = []
# while True:
#     items = input("What does your store have?")
#     if items != "end":
#         store.append(items)
#     else:
#         break
# Task 4b (refer to lines 84-91)
# wants = input("What are you looking for?")
# for items in store:
#     if wants == items:
#         print("Yes we sell that.")
#     else:
#         print("Sorry, we dont have that.")

# while True:
#     ui = input("What are you looking for? ")
#     if ui == "end":
#         break
#     if ui in store:
#         print("Yes we sell that")
#     else:
#         print("No, we don't sell that")


# Task 5: Lucky draw number generator
# Create a lucky draw number generator that generates 10 numbers
# between 1 to 9999.

# 1. Import the 'random' library
# 2. Using the 'random.randint()' function and a 'for' loop, add 10
#    random numbers into a list
# 3. Using another loop, announce the winners in the following format:
#     a. Winner #1: 5426
#     b. Winner #2: 3241
#     c. Etc...

# import random
# WinNum = []
# for i in range(10):
#     LuckNum = random.randint(1, 9999)
#     WinNum.append(str(LuckNum))
#     print("Winner #" + str(i + 1) + ": " + WinNum[i])

    # Task 6: Pizza Topping
# Create a program that asks the user what pizza topping they want

# 1. Create a list of pizza toppings
# 2. Print out the list of pizza toppings with an index number next
#    to each of them in this format:
#     "1. Mushrooms"
#     "2. Pepperoni"
#     "3. Pineapple"
#     ...
# 3. In a 'while' loop, ask the user which pizza topping they want
#    (By index)
# 4. Exit the 'while' loop only when the user enters "end"
# 5. Print the toppings that the user has selected

# 13.6 Teacher solution
# Step 1: Create a list of pizza toppings
# pizza_toppings = ["Mushrooms", "Pepperoni", "Pineapple", "Onions", "Sausage", "Bacon", "Extra cheese", "Black olives", "Green peppers", "Fresh garlic"]
# user_toppings = []

# # Step 2: Use a 'for' loop to print the list of pizza toppings without using len() or enumerate()
# print("Available pizza toppings:")
# i = 1  # Manually track the index
# for topping in pizza_toppings:
#     print(str(i) + ". " + topping)
#     i += 1  # Increment the index manually

# # Step 3: Ask the user which pizza topping they want (By index)

# while True:
#     user_choice = input("Please choose your pizza topping by number: ")
#     if user_choice == "end":
#         break
#     else:
#         user_toppings.append(pizza_toppings[int(user_choice) - 1])

# for i in user_toppings:
#     print(i)

