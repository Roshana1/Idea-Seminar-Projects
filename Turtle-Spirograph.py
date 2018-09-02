#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep
import random
from random import randrange
# http://www.101computing.net/python-turtle-spirograph/

window = turtle.Screen()
window.bgcolor("black")
m = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
R = 100
r = 10
d = 70
angle = 10
theta = 0.05

steps = int(100*3.14/theta)
for t in range(0,steps):
  m.color(colors[t%6])
  angle += theta
  x = (R - r) * cos(angle) - d * cos(((R-r)/r)*angle)
  y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
  m.goto(x,y)
  turtle.done()
