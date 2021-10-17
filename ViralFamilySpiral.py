import turtle #Set up turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "brown", "gray", "pink" ]
family = []     #Set up an empty list for family names
#Ask for the first name
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
sides = int(turtle.numinput("Number of sides",
                            "How many sides in your spiral of spirals (2-6)?", 4,2,6))
#Keep asking for names
while name != "":
    #Add their name to the family list
    family.append(name)
    #Ask for another name, or end
    name = turtle.textinput("My family",
                            "Enter a name, or just hit [ENTER] to end:")
#Draw a spiral of the names on the screen
for x in range(100):
    position = t.position()      #Remember this corner of the spiral
    heading = t.heading()       #Remember the direction we were heading
    print(position, heading)
    for n in range(int(x/2)):
            t.forward(2*n)
            t.right(360/sides - 2)
            t.penup()
    t.setx(position[0])     #Go back to the big spiral's x location
    t.sety(position[1])     #Go back to the big spiral's y location
    t.setheading(heading)   #Point in the big spiral's heading.
    t.left(360/sides + 2)   #Aim at the next point on the big spiral
    t.pencolor(colors[x%len(family)])   #Rotate throught the colors
    t.penup()                           #Don't draw the regular spiral lines
    t.forward(x*4)                      #Just move the turtle on the screen
    t.pendown()                         #Draw the next family member's name
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
    t.left(360/len(family) + 2)         #Turn left for our spiral
