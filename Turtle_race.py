from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)
for step in range(16):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(200)
    penup()
    backward(210)
    left(90)
    forward(30)

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()
for turn in range(100):
    laura.forward(randint(1,5))