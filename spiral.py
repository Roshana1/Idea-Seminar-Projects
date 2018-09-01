import rhinoscriptsyntax as rs
import math

points = []
 
for d in rs.frange(0.0, 40, 0.3):
    x = d*math.sin(d)
    y = d*math.cos(d)
    z = d + 1
    rs.AddPoint(x,y,z)
    pt = (x,y,z)
    rs.AddSphere(pt,1)
    points.append(pt)
    
 
curve = rs.AddCurve(points)

