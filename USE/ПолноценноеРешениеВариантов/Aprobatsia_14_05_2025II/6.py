from turtle import Turtle, screensize, tracer, done


t = Turtle()
t.lt(90)
screensize(2000, 2000)
m = 25
tracer(0)


t.rt(45)
for i in range(45):
    t.fd(8 * m)
    t.rt(45)
    t.fd(16 * m)
    t.rt(135)
t.up()

for x in range(-20, 30):
    for y in range(-20, 20):
        t.setpos(x * m, y * m)
        t.dot(5, "red")
done()
