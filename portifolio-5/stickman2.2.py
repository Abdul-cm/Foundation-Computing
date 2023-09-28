import turtle #turtle module
t = turtle. Turtle() #create an object called 't' of class Turtle()
def draw(x,y,size2, size3, size4, circlesize): #draw a figure, for example a stickman
    t.penup() #turn pen off
    t.setx(x) #setup a position (100, -100)
    t.sety(y)
    t.pendown() #turn pen on

    #plot the stickman
    for i in range
    (2):
        t.left(120)
        t.forward(size)

    for i in range (1):
        t.left(180)
        t.forward(size)
        t.left(130)
        t.forward(size2)
        t.right(120)

    for i in range (2):
        t.forward(size4)
        t.left(180)
        t.forward(size4)
        t.left(60)


    for i in range (1):
        t.forward(size3)
        t.right(90)
        t.circle(circlesize)

draw(100,-100,80,100,20,60,18)

   

          
                
