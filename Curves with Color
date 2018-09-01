import rhinoscriptsyntax as  rs

from Rhino import Geometry
plane = rs.WorldXYPlane()
for i in range (2,100):
    
 plane = rs.RotatePlane(plane, i / 3 , [i  ,i  , 0])
 x = i
 Arc = rs.AddArc( plane, x / 7 , i   )
 color02 = [i * 2 , i ,i * 2]
 rs.ObjectColor(Arc, color02)
