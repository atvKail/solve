# def cft(x, y, z):
#     return x + y > z and x + z > y and y + z > x

# def ate(sides1, sides2):
#     return sorted(sides1) == sorted(sides2)


# a, b, c = map(int, input().split())
# d, e, f = map(int, input().split())

# if not (cft(a, b, c) and cft(d, e, f)):
#     print(0)
# else:
#     print(1)
#     if ate([a, b, c], [d, e, f]):
#         print(1)
#     else:
#         print(0)  # A


# def is_convex_quadrilateral(points):
#     Ax, Ay = points[0]
#     Bx, By = points[1]
#     Cx, Cy = points[2]
#     Dx, Dy = points[3]

#     ABBC = (Bx - Ax) * (Cy - By) - (Cx - Bx) * (By - Ay)
#     BCCD = (Cx - Bx) * (Dy - Cy) - (Dx - Cx) * (Cy - By)
#     CDDA = (Dx - Cx) * (Ay - Dy) - (Ax - Dx) * (Dy - Cy)
#     DAAB = (Ax - Dx) * (By - Ay) - (Bx - Ax) * (Ay - Dy)

#     return (ABBC > 0 and BCCD > 0 and CDDA > 0 and DAAB > 0) or \
#            (ABBC < 0 and BCCD < 0 and CDDA < 0 and DAAB < 0)


# def can_inscribe_circle(points):
#     def distance(p1, p2):
#         return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

#     if not is_convex_quadrilateral(points):
#         return False

#     AB = distance(points[0], points[1])
#     BC = distance(points[1], points[2])
#     CD = distance(points[2], points[3])
#     DA = distance(points[3], points[0])

#     return abs((AB + CD) - (BC + DA)) < 1e-6


# Ax, Ay = map(int, input("Введите координаты точки A (Ax Ay): ").split())
# Bx, By = map(int, input("Введите координаты точки B (Bx By): ").split())
# Cx, Cy = map(int, input("Введите координаты точки C (Cx Cy): ").split())
# Dx, Dy = map(int, input("Введите координаты точки D (Dx Dy): ").split())

# points = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]

# if can_inscribe_circle(points):
#     print("Окружность можно вписать в четырёхугольник.")
# else:
#     print("Окружность нельзя вписать в четырёхугольник.")

