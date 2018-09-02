import turtle
import random
t = turtle.Turtle()

#get the number and size of squars
a = input("insert the size")
b = input("insert the steps")

#draw each square with a random distance from the last one
for x in xrange(int(b)):
   a = int(a) + 10
   t.penup()
   c = random.randint(1,50)
   d = random.randint(1,50)
   #e = random.randint(20,300)
   t.forward(c)
   t.left(90)
   t.forward(d)
   t.pendown()
   R = random.randrange(0, 257, 10)
   B = random.randrange(0, 257, 10)
   G = random.randrange(0, 257, 10)
   t.color((R, G, B))

# drawing the squares
   for i in xrange(4):
      t.forward(a)
      t.left(90)