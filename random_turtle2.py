import turtle
import random
turtle.speed(1)
turtle.shape("turtle")
turtle.colormode(255)
for i in range(50):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.pencolor(r,g,b)
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    #set a random position 
    turtle.setposition(x,y)
    #set a random color
    i = random.randint(0,len(colors))
    turtle.pencolor(colors[i])
    turtle.done()
    