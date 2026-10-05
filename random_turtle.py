import turtle 
import random

turtle.shape("turtle")
colors = ["yellow","blue","red","orange","purple","pink","black"]

for i in range(20):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    turtle.setposition(x,y)
    turtle.dot()


turtle.speed(1)

turtle.done()