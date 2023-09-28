#draw stickman
import turtle
t = turtle.Turtle()
def drawstickman(x,y,size):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.circle(40)
    t.right(90)
    t.forward(170)
    t.left(40)
    t.forward(60)
    t.backward(60)
    t.right(80)
    t.forward(90)
    t.backward(90)
    t.left(220)
    t.forward(115)
    t.right(40)
    t.forward(60)
    t.backward(60)
    t.left(80)
    t.forward(60)
    t.left(220)
# set position
for x in range (0,420,103):
     drawstickman(x,-200,100)
