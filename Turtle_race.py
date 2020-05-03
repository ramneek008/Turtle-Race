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
else:
    write('END', align="center")
    right(90)
    forward(10)
    pendown()
    forward(220)
    penup()
    backward(230)
    left(90)
    forward(30)

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
for turn in range(4):
    laura.right(90)
laura.pendown()

peter = Turtle()
peter.color('green')
peter.shape('turtle')
peter.penup()
peter.goto(-160,50)
for turn in range(4):
    peter.right(90)
peter.pendown()


rik = Turtle()
rik.color('blue')
rik.shape('turtle')
rik.penup()
rik.goto(-160,0)
for turn in range(4):
   rik.right(90)
rik.pendown()

bruno = Turtle()
bruno.color('yellow')
bruno.shape('turtle')
bruno.penup()
bruno.goto(-160,-50)
for turn in range(4):
    bruno.right(90)
bruno.pendown()

sum1 = sum2 = sum3 = sum4 = 0

for movement in range(150):
    p = randint(1,5)
    sum1 = sum1+p
    laura.forward(p)

    q = randint(1,5)
    sum2 = sum2+q
    peter.forward(q)

    r = randint(1,5)
    sum3 = sum3+r
    rik.forward(r)

    s = randint(1,5)
    sum4 = sum4+s
    bruno.forward(s)

    if(sum1>=420 or sum2>=420 or sum3>=420 or sum4>=420):
        break;


ranks = {'Laura (red)':sum1 , 'Peter (green)':sum2, 'Rik (blue)':sum3, 'Bruno (yellow)':sum4}
v = list(ranks.values()) 
k = list(ranks.keys()) 
  
print(k[v.index(max(v))], "wins the race.") 



input()