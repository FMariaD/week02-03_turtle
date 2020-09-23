import turtle as tur
import numpy as np

tur.shape('turtle')
tur.color('purple')
tur.speed(10)
print ('Параметр k')
k = float (input())
print ('Количество витков спирали')
n = float (input())

def f(x):
     return ((k*(1 + 2*3.1415*x/360))**1/2)*1
 
m = n*k * np.pi
i = 1 
z = 0
while z <= m:
    tur.left(1)
    tur.forward(f(i))
    z = f(i)
    i += 1 
