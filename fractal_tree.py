from turtle import *
angle = 35
t = Turtle()
t.speed(0)
t.hideturtle()

def f(l):
	ox = t.xcor()
	oy = t.ycor()
	if (l > 1):
		t.rt(angle)
		t.fd(l)
		f(l*0.66)
		t.goto(ox,oy)
		t.lt(angle)

		t.lt(angle)
		t.fd(l)
		f(l*0.66)
		t.goto(ox,oy)
		t.rt(angle)

t.home()
t.clear()
t.lt(90)
t.bk(150)
t.fd(150)
f(100)
