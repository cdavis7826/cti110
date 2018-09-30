# Write a code to draw your initials
# CTI-110
# Chad Davis
# 9/26/18
# (Import turtle
#  Set variables for background color,
#  pen size and pen color
#  

import turtle

wn = turtle.Screen()
wn.bgcolor('Blue') # background color


chad = turtle.Turtle()
chad.pensize(5)  #pen size and pen color
chad.color('white')

chad.forward(200)  # code for the letter C
chad.left(90)
chad.forward(50)
chad.left(90)
chad.forward(150)
chad.right(90)
chad.forward(200)
chad.right(90)
chad.forward(150)
chad.left(90)
chad.forward(50)
chad.left(90)
chad.forward(200)
chad.left(90)
chad.forward(300)
chad.left(90)

chad.penup() # Code for the outer part of letter D
chad.forward(275)
chad.pendown()
chad.forward(175)
chad.left(45)
chad.forward(75)
chad.left(45)
chad.forward(195)
chad.left(45)
chad.forward(75)
chad.left(45)
chad.forward(175)
chad.left(90)
chad.forward(300)

chad.penup()  # # Code for the inner part of letter D
chad.left(90)
chad.forward(50)
chad.left(90)
chad.forward(50)
chad.pendown()
chad.forward(200)
chad.right(90)
chad.forward(100)
chad.right(45)
chad.forward(50)
chad.right(45)
chad.forward(130)
chad.right(45)
chad.forward(50)
chad.right(45)
chad.forward(100)



