from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()

peter = Turtle()
peter.color('green')
peter.shape('turtle')
peter.penup()
peter.goto(-160,70)
peter.pendown()

lethal = Turtle()
lethal.color('blue')
lethal.shape('turtle')
lethal.penup()
lethal.goto(-160,40)
lethal.pendown()

rik = Turtle()
rik.color('yellow')
rik.shape('turtle')
rik.penup()
rik.goto(-160,10)
rik.pendown()

for movement in range(100):
    laura.forward(randint(1,5))
    peter.forward(randint(1,5))
    lethal.forward(randint(1,5))
    rik.forward(randint(1,5))


input("Press Enter to close")