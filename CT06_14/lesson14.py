# print("Hello from lesson 15")

import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("red")
for i in range(4):
    t.forward(50)
    t.left(90)
window.mainloop()
