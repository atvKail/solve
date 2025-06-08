from turtle import *


screensize(2000, 2000)
tr = Turtle()
m = 10
tracer(0)

tr.lt(90)
for _ in range(3):
    tr.fd(10 * m)
    tr.rt(90)
    tr.fd(15 * m)
    tr.rt(90)
tr.up()
tr.fd(4 * m)
tr.rt(90)
tr.fd(7 * m)
tr.lt(90)
tr.down()
for _ in range(2):
    tr.fd(80 * m)
    tr.rt(90)
    tr.fd(60 * m)
    tr.rt(90)
tr.up()

for i in range(-60, 30):
    for j in range(-100, 30):
        tr.setpos((i * m, j * m))
        tr.dot(5, "red")
done()