from random import *
import turtle as t

number_of_turtles = 20

t.penup()
t.goto(-250, 250)
t.pendown()
for i in range (4):
    t.forward(500)
    t.right(90)

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
t.turtlesize(0.7)
for unit in pool:
    unit.turtlesize(0.7)
    unit.penup()
    unit.speed(200)
    unit.goto(randint(-250, 250), randint(-250, 250))
    unit.seth(randint(0, 360))

while True:
    for unit in pool:
        unit.forward(randint(1, 10))
        if abs(unit.xcor()) >= 249:
            unit.seth(180 - unit.heading())
            unit.forward(10)
        if abs(unit.ycor()) >= 249:
            unit.seth(360 - unit.heading())
            unit.forward(10)
