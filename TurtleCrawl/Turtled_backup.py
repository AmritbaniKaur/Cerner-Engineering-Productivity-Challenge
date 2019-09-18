#cerner_2^5_2019
from mobilechelonian import Turtle
turtle = Turtle()
turtle.speed(40)
colours=["red","yellow"]

turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.pendown()

for i in range (0,18):
    turtle.pencolor(colours[i%2])
    turtle.right(20)
    turtle.forward(20)

turtle.right(180)
turtle.home()

