# print("Hello from lesson 15")

import turtle
window = turtle.Screen
t = turtle.Turtle
window.setup(width=600, height=400)
counter = input("Number of sides?")
for i in range(counter):
    t.forward(50)
    t.left(360 / counter)