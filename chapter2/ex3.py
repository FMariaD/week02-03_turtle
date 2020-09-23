import turtle as t

t.shape('turtle')
t.speed(1)
t.color('green')
t.width(3)

s = input()
start = [-300, 0]

def draw_number(xy, start):
    t.penup()
    t.goto(*start)
    t.pendown()
    x0, y0 = start
    for x, y in xy:
        t.goto(x + x0, y + y0)

xy = open('config.txt', 'r')
for i in range(len(s)):
    if (s[i]==' '):
        i += 1
    else:
        b = s[i]
        b = int(b)
        k = readline(b+1)
        draw_number(k, start)
        start[0] += 90
close('config.txt')
