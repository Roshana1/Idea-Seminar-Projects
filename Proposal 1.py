
import rhinoscriptsyntax as rs
import math

points = []
for i in rs.frange(0,3, 0.1):
  i = i + 1    
  for d in rs.frange(0,5, 0.1):
    x = d * 2
    y = math.cos(x)
    z = i * d  
    pt = (x,y,z)
    points.append(pt)
    
 
curve = rs.AddCurve(points)
