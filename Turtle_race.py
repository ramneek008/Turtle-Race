from turtle import *

penup()
goto(-140,140)
for step in range(6):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(200)
    penup()
    backward(210)
    left(90)
    forward(30)
