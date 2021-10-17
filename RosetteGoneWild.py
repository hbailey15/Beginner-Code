# Rosette.py - draws a rosette

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "blue", "green", "purple", "pink", "white"]
# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles is your rosette?", 6))
for x in range(number_of_circles):
    t.pencolor(colors[x%6])
    t.circle(100)
    t.left(360/number_of_circles)

more_circles = int(turtle.numinput("Number of tiny circles",
                                   "How many tiny circles is your rosette?", 6))
for x in range(more_circles):
    t.pencolor(colors[x%6])
    t.circle(30)
    t.left(360/more_circles)

    
    
