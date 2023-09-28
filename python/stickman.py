#Task 2.4 animate stickman
import turtle
import time
t = turtle.Turtle()
s = turtle.Screen()
s.tracer(0)
xpos = 350
ypos = 200
angle = 0
for x in range(37):# to move stickman through the x-axis
    t.clear()
    t.penup()
    t.setpos(xpos,ypos)
    t.setheading(angle)
    t.pendown()
    #stickman
    t.circle(40)
    t.right(90)
    t.forward(170)
    t.left(40)
    t.forward(80)
    t.backward(80)
    t.right(80)
    t.forward(80)
    t.backward(80)
    t.left(220)
    t.forward(115)
    t.right(40)
    t.forward(60)
    t.backward(60)
    t.left(80)
    t.forward(60)
    #moving animation
    xpos = xpos -20
    ypos = ypos -8
    angle = angle + 25
    s.update()
    time.sleep(0.2)
