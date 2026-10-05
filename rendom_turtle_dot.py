import turtle
import random
turtle.penup()
turtle.colormode(255)

for i in range(50):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.pencolor(r,g,b)
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle.setposition(x,y)
    turtle.dot()
turtle.done()