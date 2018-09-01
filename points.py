import rhinoscriptsyntax as rs
import math
from Rhino import Geometry


Points = rs.GetPoint("Pick a starting point")
Points = []
for d in rs.frange(0.0, 40, 0.3):
    x = d*math.sin(d)
    y = d*math.sin(d)
    z = d + 1
    rs.AddPoint(x,y,z)
    pt = (x,y,z)
    Points.append(pt)

myCurve = rs.AddCurve(Points)
color02 = [255,0,255] #magenta
rs.ObjectColor(myCurve, color02)

Points2 = []
for d in rs.frange(0.0, 40, 0.3):
    x = d*math.sin(d)
    y = d*math.sin(d) + 30
    z = d + 1
    rs.AddPoint(x,y,z)
    pt = (x,y,z)
    Points2.append(pt)

myCurve2 = rs.AddCurve(Points2)
color02 = [255,0,255] 
rs.ObjectColor(myCurve2, color02)

