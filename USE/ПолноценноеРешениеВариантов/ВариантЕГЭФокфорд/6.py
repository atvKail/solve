import turtle
from shapely.geometry import Polygon, Point


window = turtle.Screen()
window.title("Траектория Черепахи")
t = turtle.Turtle()
t.speed(0)


t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(90)


coordinates = [(0, 0)]


for _ in range(9):
    t.forward(5)
    coordinates.append(t.position())
    t.right(50)
    t.forward(10)
    coordinates.append(t.position())
    t.right(130)


turtle.done()


polygon = Polygon(coordinates)


min_x = min(coord[0] for coord in coordinates)
max_x = max(coord[0] for coord in coordinates)
min_y = min(coord[1] for coord in coordinates)
max_y = max(coord[1] for coord in coordinates)


count = 0
for x in range(int(min_x), int(max_x) + 1):
    for y in range(int(min_y), int(max_y) + 1):
        if polygon.contains(Point(x, y)):
            count += 1

print(f"Количество точек с целочисленными координатами внутри области: {count}")
