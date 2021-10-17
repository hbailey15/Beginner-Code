import turtle
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of sides",
                            "How many sides in your spiral of spirals (2-6)?", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for m in range(100):
    t.forward(m*4)
    position = t.position()      #Remember this corner of the spiral
    heading = t.heading()       #Remember the direction we were heading
    print(position, heading)
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0])     #Go back to the big spiral's x location
    t.sety(position[1])     #Go back to the big spiral's y location
    t.setheading(heading)   #Point in the big spiral's heading.
    t.left(360/sides + 2)   #Aim at the next point on the big spiral
