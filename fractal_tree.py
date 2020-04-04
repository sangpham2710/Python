from turtle import *
angle = 90
t = Turtle()
def setup():
    t.speed(0)
    t.hideturtle()
    t.getscreen().delay(0)
    t.getscreen().tracer(0)
    t.home()
    t.clear()
    t.lt(90)
    t.bk(150)
    t.fd(150)
def draw(l):
    ox = t.xcor()
    oy = t.ycor()
    if (l > 1):
        t.rt(angle)
        t.fd(l)
        draw(l * 2 / 3)
        t.goto(ox, oy)
        t.lt(angle)                                    
        t.lt(angle)
        t.fd(l)                                   
        draw(l * 2 / 3)
        t.goto(ox, oy)
        t.rt(angle)
setup()
draw(100)
