#Draws a picture of the olympic rings logo

import turtle

my_turtle = turtle.Turtle()     #creates a pen
my_turtle.width(10)             #sets the pen width to 10

#Black ring
my_turtle.circle(100)           #draws a black circle of radius 100

#Blue ring
my_turtle.up()                  #lifts up the pen
my_turtle.backward(225)         #moves backward 225 without drawing
my_turtle.color('blue')         #sets the color blue
my_turtle.down()                #puts the pen down
my_turtle.circle(100)           #draws a blue circle of radius 100

#Red ring
my_turtle.up()                  #lifts up the pen
my_turtle.forward(450)          #moves forward 450 without drawing
my_turtle.color('red')          #sets the color red
my_turtle.down()                #puts the pen down
my_turtle.circle(100)           #draws a red circle of radius 100

#Green ring
my_turtle.up()                  #lifts up the pen
my_turtle.left(90)              #changes direction to the left 90 degrees
my_turtle.forward(100)          #moves forward 100 without drawing
my_turtle.left(90)              #changes direction to the left 90 degrees
my_turtle.forward(115)          #moves forward 115 without drawing
my_turtle.color('green')        #sets the color green
my_turtle.down()                #puts the pen down
my_turtle.circle(100)           #draws a green circle of radius 100

#Yellow ring
my_turtle.up()                  #lifts up the pen
my_turtle.forward(225)          #moves forward 225 without drawing
my_turtle.color('yellow')       #sets the color yellow
my_turtle.down()                #puts the pen down
my_turtle.circle(100)           #draws a yellow circle of radius 100
