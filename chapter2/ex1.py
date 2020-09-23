from random import *
import turtle as t

t.shape('turtle')
t.speed(3)
t.color('red')

for i in range(100):
    length = randint(0, 80)
    angle = randint(0, 360)
    t.left(angle)
    t.forward(length)
