# print("Hello from lesson 15")

import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.setup(width=600, height=400)
for i in range(5):
    t.forward(50)
    t.left(72)
window.mainloop()