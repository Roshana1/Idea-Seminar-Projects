import rhinoscriptsyntax as rs
import math
points = []
YAxis = rs.WorldXYPlane()
vector = (0,1,0)
point = rs.AddPoint(3,-10,0.5)
   
for d in rs.frange(0,3, 0.1):
    x = d 
    y =  -(math.cosh(x))
    z = 1 
    pt = (x,y,z)
    points.append(pt)
curve = rs.AddCurve(points)

for i in range(0,200):
 rs.RotateObject(curve, point, i, vector, copy=True)