import turtle as t

t.screensize(2000, 2000)
t.tracer(0)
k = 30
t.up()
for x in range(-30, 10):
    for y in range(-30, 10):
        t.goto(x*k, y*k)
        t.dot()

t.color('red')
t.home()
t.down()
t.left(90)

# Алгоритм из условия
t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*k)
    t.right(45)
t.right(315)
t.forward(10*k)
for i in range(2):
    t.right(90)
    t.forward(10*k)

t.update()
t.done()
