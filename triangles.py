import turtle as t

t.shape("turtle")
t.pencolor("green")
t.color("green")

def tri1():
    t.fd(50)
    t.right(90)
    t.fd(50)

t.fd(50)
t.left(90)
t.fd(50)
t.home()

t.left(180)
tri1()
t.home()
t.penup()
t.goto(-50, 50)
t.pendown()
t.left(90)
tri1()
t.goto(-50, 50)

t.hideturtle()
t.exitonclick()