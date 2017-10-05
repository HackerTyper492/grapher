import math
import turtle
pen=turtle.Pen()
d = 10 #domain
r = 10 #range
p = 2 #accuracy
pen.up()

def f(x):
    if (x < -d): #places where the function gives error
        y = 0
    else:
        y = x**2-10 #function
    return y

# Axes + arrows
h = 300 #horizontal length
v = 200 #vertical length
a = 8 #arrow size
pen.goto(-h, 0)
pen.down()
pen.goto(-h+a, a)
pen.goto(-h+a, -a)
pen.goto(-h, 0)
pen.goto(h, 0)
pen.goto(h-a, a)
pen.goto(h-a, -a)
pen.goto(h, 0)
pen.up()
pen.goto(0, v)
pen.down()
pen.goto(a, v-a)
pen.goto(-a, v-a)
pen.goto(0, v)
pen.goto(0, -v)
pen.goto(a, -v+a)
pen.goto(-a, -v+a)
pen.goto(0, -v)
pen.up()

#Function graphing
zero = False
x = -h+a
pen.goto(x, 0)
for i in range(int(x/p), int(-x/p)):
    x = (d/h)*(i*p)
    y = f(x)
    if (abs(f(x)-f((d/h)*((i-1)*p))) > r) or (abs(y) > r):
        pen.up()
        pen.goto(i*p, 0)
        print("out of range")
    else:
        pen.goto(i*p, ((v-a)/r)*y)
        pen.down()
        print( (y-f((d/h)*((i-1)*p))) )
