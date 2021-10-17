#RosettesAndPolygons.py - a spiral of polygons and rosettes
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
#Ask the user for the number of sides, default to 4
sides = int(turtle.numinput("Number of sides",
                            "How many sides in your spiral between 2-8?", 4, 2, 8))
colors = ["red", "yellow", "orange", "green", "pink", "white", "blue", "purple"]
#Our outer spiral loop for polygons and rosettes from size 5 to 75
for m in range(5,75):
    t.left(360/sides + 2)
    t.width(m//25+1)
    t.penup()       #Don't draw lines on spiral
    t.forward(m*4)  #Move next corner
    t.pendown()     #Get ready to draw
    #Draw a little rosette at each EVEN corner of the spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.pencolor(colors[n])
            t.circle(m/3)
            t.right(360/sides)
    #OR, draw a little polygon at each ODD corner of the spiral
    else:
        for n in range(sides):
            t.pencolor(colors[n])
            t.forward(m)
            t.right(360/sides)
