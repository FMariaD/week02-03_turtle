import turtle as tur

tur.shape('turtle')
tur.color('blue')
d = 10     
for i in range (0, 25):  
    tur.forward(d)
    tur.left(90)
    tur.forward(d)
    tur.left(90)
    d += 10
    i += 1
