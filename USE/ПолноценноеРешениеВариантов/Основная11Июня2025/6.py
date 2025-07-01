import turtle


tr = turtle.Turtle()
turtle.screensize(2000, 2000)
turtle.tracer(0)

m = 10

tr.setposition(0, 0)
tr.lt(90)

for _ in range(2):
    tr.fd(20 * m)
    tr.lt(270)
    tr.fd(12 * m)
    tr.rt(90)
tr.up()
tr.fd(9 * m)
tr.rt(90)
tr.fd(7 * m)
tr.lt(90)
tr.down()
for _ in range(2):
    tr.fd(13 * m)
    tr.rt(90)
    tr.fd(6 * m)
    tr.rt(90)

tr.up()
for i in range(-30 * m, 30 * m, m):
    for j in range(-30 * m, 30 * m, m):
        tr.setpos((i, j))
        tr.dot(5, "red")
turtle.done()

# 21 * 13 + 7 * 14 - 12 * 6 = 299
# Ответ 299
