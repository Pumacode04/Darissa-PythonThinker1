# print("Hello from lesson 15")

# import turtle
# window = turtle.Screen()
# t = turtle.Turtle()
# window.setup(width=600, height=400)
# for i in range(5):
#     t.forward(50)
#     t.left(72)
# window.mainloop()

import random
import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.setup(width=600, height=600)
t.shape("turtle")
t.color("orange")
for i in range(10):
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    t.goto(x, y)
    for i in range(4):
        t.forward(5)
        t.left(90)
    t.up
    t.sety(y - 40)
    
    t.write(str(x) + ", " + str(y))
window.mainloop()