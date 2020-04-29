from turtle import *
from random import randint

speed(10)


penup()
goto(-140,140)
for step in range(15):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(210)
    penup()
    backward(220)
    left(90)
    forward(30)

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

peter = Turtle()
peter.color('green')
peter.shape('turtle')
peter.penup()
peter.goto(-160,50)
peter.pendown()


rik = Turtle()
rik.color('blue')
rik.shape('turtle')
rik.penup()
rik.goto(-160,0)
rik.pendown()

bruno = Turtle()
bruno.color('yellow')
bruno.shape('turtle')
bruno.penup()
bruno.goto(-160,-50)
bruno.pendown()


for movement in range(150):
    laura.forward(randint(1,5))
    peter.forward(randint(1,5))
    rik.forward(randint(1,5))
    bruno.forward(randint(1,5))


input()