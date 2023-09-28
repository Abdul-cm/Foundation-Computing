import turtle
i = turtle.Turtle() #create an object called 'i' of class Turtle()
def drawinitials(x,y, size, size2, size3, size4): #draw my initials an A and I
    i.penup () #turn pe
    i.setx(x) #setup a position (100, 100)
    i.sety(y)
    i.pendown() #turn pen on

    #plot the initials
    for f in range (2):
        i.left(120)
        i.forward(size)

    for f in range (1):
        i.left(180)
        i.forward(size2)
        i.right(60)
        i.forward(size2)
        i.penup()
        i.forward(size)
        i.right(90)
        i.forward(size3)
        i.left(180)
        i.pendown()
        i.forward(size4)
        i.penup()
        i.left(90)
        i.forward(size2)
        i.right(180)
        i.pendown()
        i.forward(size)
    

drawinitials(100, 100, 200, 100, 85, 185)

        


    
    
