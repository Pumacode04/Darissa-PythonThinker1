print("Hello from lesson 15")

import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
for i in range(4):
    t.forward(50)
    t.left(100)
window.mainloop()
