# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "white"]
turtle.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
sides = eval(input("Enter a number of sides between 2 and 8: "))
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.left(90)
    t.width(x*sides/200)
