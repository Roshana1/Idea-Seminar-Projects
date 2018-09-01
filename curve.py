import rhinoscriptsyntax as rs
import random
pt = rs.GetPoint("Pick starting point")
num = rs.GetInteger("Enter a the number of iterations" )
points = []
def Circles(pt, r):
    if num == 0:
     return 0
    else:
     for i in range (0,num):
         i = i + 1
     for p in range (0,5):
             x = random.uniform(pt.x - 10, pt.x + 10)
             y = random.uniform(pt.y - 10, pt.y + 10)
             z = random.uniform(pt.z - 10, pt.z + 10)
             pt = (x,y,z)
             points.append(pt)

curve = rs.AddCurve(points)
pt = rs.GetPoint("Pick starting point")
num = rs.GetInteger("Enter a the number of iterations" )
