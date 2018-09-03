import turtle
import random


turtle.tracer(False)
t = turtle.Turtle()
m = turtle.Turtle()
turtle.hideturtle()
t.color("red")
#get the number and size of squars
a = input("insert the size")
# b = input("insert the steps")
r = 40 * float(a)
t.left(200)
t.circle(r , 320)
t.right(80)
t.forward(25 * float(a))
t.left(160)
for i in xrange(2):
  t.forward(20 * float(a))
  t.right(140)
  t.forward(20 * float(a))
  t.left(150)
t.forward(30 * float(a))

# defins how to draw a petal 
def petal(r,step):
    m.circle(20 * float(a) ,150)
    m.left(50)
    m.circle(20 * float(a),150)
m.color("red")
m.penup()
m.setx(r / 3)
m.sety(-r * 1.7)
m.pendown()

# defins how to draw a flower 
def flower():
 m.color("red")
 m.penup()
 m.setx(r / 3)
 m.sety(-r * 1.7)
 m.pendown()
 for i in xrange (13):
    m.setheading(0)
    m.left(30 * i)
    petal(10,8)
flower()  
