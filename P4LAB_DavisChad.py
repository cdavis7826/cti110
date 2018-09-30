# Create a turtle graphics program that draws a shape using a nested loop.
# CTI-110 P4LAB_NestedLoops
# 9/29/18
# Chad Davis
#
# (Psuedocode - Start turtle program,
#  Set value for turtle as star,
#  Set line thickness,
#  Enter "for" loop and "range" to start initial arm,
#  Enter nested "for" loop and "range" for smaller lines on each arm,
#  Have arrow return to point of origin and move to correct position for
#  Continuation of loop,
#  Enter code for for window to close on click.)


import turtle
# Set turtle value.
star = turtle.Turtle()

# Set pen thickness.
star.pensize(5)

# "for" loop and "range" loop for intial arm of drawing.
for i in range(8):
    star.forward(250)

    # Nested loop for drawings on each arm.
    for i in range(8):
        star.back(30)
        star.left(45)
        star.forward(30)

    # Bring arrow back to original point of origin and move to start new arm.
    star.back(250)    
    star.left(45)

turtle.exitonclick()



    
