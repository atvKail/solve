import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-60, -10, 110, 130)

# Черепаха для рисования фигур
drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()


def draw_rectangle(x, y, width, height, color="black"):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color)
    drawer.goto(x + width, y)
    drawer.goto(x + width, y + height)
    drawer.goto(x, y + height)
    drawer.goto(x, y)
    drawer.penup()


draw_rectangle(0, 0, 101, 77, "black")

draw_rectangle(-44, 29, 75, 88, "blue")

# Для Фигуры A (прямоугольник):
#   x ∈ [0, 101] и y ∈ [0, 77] → внутренняя область: x ∈ (0, 101), y ∈ (0, 77)
#
# Для Фигуры B:
#   x ∈ [-44, 31] и y ∈ [29, 117] → внутренняя область: x ∈ (-44, 31), y ∈ (29, 117)
#
# Пересечение внутренних областей определяется по осям:
#   По x: (max(0, -44), min(101, 31)) = (0, 31)
#   По y: (max(0, 29), min(77, 117)) = (29, 77)
#
# Область пересечения (с границами): от (0,29) до (31,77),
# а внутренняя (без границ) – x ∈ (0,31), y ∈ (29,77)
intersection_x_min = 0
intersection_x_max = 31
intersection_y_min = 29
intersection_y_max = 77

drawer.color("red")
drawer.penup()
drawer.goto(intersection_x_min, intersection_y_min)
drawer.pendown()
for _ in range(2):
    drawer.forward(intersection_x_max - intersection_x_min)
    drawer.left(90)
    drawer.forward(intersection_y_max - intersection_y_min)
    drawer.left(90)
drawer.penup()

# --- Отметим целые точки, лежащие строго внутри пересечения ---
# Искомые точки – те, у которых x и y целые, и:
#   x ∈ (0,31)  → целые x: 1, 2, ..., 30  (30 значений)
#   y ∈ (29,77) → целые y: 30, 31, ..., 76 (47 значений)
# Общее число точек = 30 * 47 = 1410.
count = 0
point_marker = turtle.Turtle()
point_marker.hideturtle()
point_marker.speed(0)
point_marker.color("green")
point_marker.penup()

for x in range(intersection_x_min + 1, intersection_x_max):
    for y in range(intersection_y_min + 1, intersection_y_max):
        point_marker.goto(x, y)
        point_marker.dot(3)
        count += 1

drawer.goto(-40, -5)
drawer.color("purple")
drawer.write(
    f"Количество целых точек внутри пересечения: {count}", font=("Arial", 16, "normal")
)

turtle.done()
