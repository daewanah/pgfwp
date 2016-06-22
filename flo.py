import turtle

window = turtle.Screen()
window.bgcolor ("black")

arw = turtle.Turtle()
arw.shape("arrow")
arw.color("green")
arw.speed(6)

for i in range (1,37):
    arw.left(35)
    arw.forward(50)
    arw.right(35)
    arw.forward(50)
    arw.right(145)
    arw.forward(50)
    arw.right(35)
    arw.forward(50)
    arw.right(10)
arw.seth(270)
arw.forward(200)

window.exitonclick()
