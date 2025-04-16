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

food = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Honey"]
food[7] = "Herbs"
food.append("Ice")
food.insert(1, "Bananas")
food.pop(2)
# OR
# del(food[2])
print(food)