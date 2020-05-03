import turtle
import random

turtle.title('거북이로 소라모양 그리기')
turtle.shape('turtle')
turtle.goto(0, 0)
turtle.pendown()
turtle.speed(10)
turtle.pensize(3)

r, g, b = 0, 0, 0
line, i = 5, 0

for i in range(0, 80, 1):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    line = line + 1
    turtle.forward(line)
    turtle.left(30)

turtle.done()


