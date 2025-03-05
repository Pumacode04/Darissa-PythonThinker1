# Task 1
# Name = input("What is your name?")
# # The step above is just asking for your name
# print("Nice to meet you, " + Name + "!")
# This other step above you is just saying "Nice to meet you," which is what it is supposed
# # (continue from previous comment) say and the name you typed in eariler.

# Task 2
Start = int(input("State your first number."))
Stop = int(input("State your second number."))
Increment = int(input("State your last number now."))
# The top three codes are storing your choice of numbers in a variable
for i in range(Start, Stop, Increment):
    print(i)