import turtle

turtle.bgcolor("black")
turtle.pensize(2)

for i in range(6):
    for colours in ["red", "magenta", "blue", "green", "yellow", "whith"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)


turtle.hideturtle()
