from turtle import *
from random import randint

speed(10)
head = Turtle()
head.penup()
head.goto(60,200)
head.pendown()
head.color('black')
style = ('Comic Sans', 30, 'bold italic')
head.write('Turtle Race', font=style, align='center')
head.hideturtle()
penup()

file_obj = open("asciiart.txt")
x = file_obj.read()
print (x) 

goto(-140,140)
for step in range(15):
    write(step, align="center")
    right(90)
    forward(10)
    for dash in range(22):
        speed(100)
        if(dash%2==0):
            pendown()
        else:
            penup()
        forward(10)
    backward(230)
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