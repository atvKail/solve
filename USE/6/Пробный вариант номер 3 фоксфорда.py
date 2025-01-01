import turtle
import math

def draw_grid():
    turtle.speed(0)
    turtle.penup()
    grid_size = 300
    step = 20

    turtle.color("lightgray")
    for x in range(-grid_size, grid_size + 1, step):
        turtle.goto(x, -grid_size)
        turtle.pendown()
        turtle.goto(x, grid_size)
        turtle.penup()

    for y in range(-grid_size, grid_size + 1, step):
        turtle.goto(-grid_size, y)
        turtle.pendown()
        turtle.goto(grid_size, y)
        turtle.penup()

def simulate_turtle_path():
    turtle.speed(1)
    turtle.color("black")

    x, y = 0, 0
    angle = 90

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    path = [(x, y)]

    for _ in range(9):
        turtle.setheading(angle)
        turtle.forward(5 * 20)
        x, y = turtle.position()
        path.append((x, y))

        angle -= 50

        turtle.setheading(angle)
        turtle.forward(10 * 20)
        x, y = turtle.position()
        path.append((x, y))

        angle -= 130

    return path

screen = turtle.Screen()
screen.setup(width=800, height=800)

draw_grid()

simulate_turtle_path()

screen.mainloop()
