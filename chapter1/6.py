import turtle as tur

tur.shape('turtle')
tur.color('purple')
n = int (input())
b = 360/n
for i in range (0, n):
    tur.forward(75)
    tur.stamp()
    tur.backward(75)
    tur.left(b)
    i += 1
