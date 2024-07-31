import turtle as t

k = 25
t.screensize(1000, 1000)
t.tracer(0)
t.penup()

for x in range(-10, 20):
    for y in range(-10, 20):
        t.goto(x * k, y * k)
        t.dot()


t.color('red')
t.home()
t.left(90)
t.pendown()

for i in range(7):
    t.right(90)
    t.circle(4 * k, -180)
    t.right(180)

t.update()
t.done()