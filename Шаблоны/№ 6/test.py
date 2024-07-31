import turtle as t

t.screensize(2000, 2000)
t.tracer(0)
k = 30
t.up()
for x in range(-30, 20):
    for y in range(-30, 20):
        t.goto(x*k, y*k)
        t.dot()

t.color('red')
t.home()
t.down()
t.left(90)

# Алгоритм из условия
for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.up()
t.forward(5*k)
t.right(90)
t.forward(7*k)
t.left(90)
t.down()
for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)

t.update()
t.done()
