import turtle as t

t.shape("turtle")
t.pencolor("green")
t.color("green")

def tri1():
    t.fd(50)
    t.right(90)
    t.fd(50)

#bottom right triangle
t.begin_fill()
t.fd(50)
t.left(90)
t.fd(50)
t.home()
t.end_fill()

#bottom left triangle
t.begin_fill()
t.left(180)
tri1()
t.home()
t.end_fill()
t.penup()
t.goto(-50, 50)
t.pendown()

#top left triangle
t.begin_fill()
t.left(90)
tri1()
t.goto(-50, 50)
t.end_fill()
t.penup()
t.goto(0, 100)
t.pendown()

#top right triangle
t.begin_fill()
t.fd(50)
t.right(90)
t.fd(50)
t.goto(0, 100)
t.end_fill()

t.hideturtle()
t.exitonclick()