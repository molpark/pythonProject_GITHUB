import turtle

t = turtle.Pen()
t.width(3)
t.speed(0)
mycolor=["red","yellow","blue","green"]
for i in range(1,30):
    t.penup()
    t.goto(0,-10*i)
    t.pendown()
    t.color(mycolor[i%len(mycolor)])
    t.circle(i*10+10)

turtle.done()