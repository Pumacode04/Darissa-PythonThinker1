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

# food = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Honey"]
# for foods in food:
#     if foods == "Apples":
#         print(foods) + ": I need 5 of these")
#     elif foods == "Carrots":
#         print(foods) + ": I need 3 of these")
#     elif foods == "Grapes":
#         print(foods) + ": Get the FarmFresh brand")
#     else:
#         print(foods)

basket = []
while True:
    food = input("What do you want to add?")
    if food != "end":
        basket.append(food)
    else:
        break
for foods in food:
    print("I have bought " + food)