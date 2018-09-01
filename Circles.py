import rhinoscriptsyntax as rs

def Circles(pt, r):
    if num == 0:
     return 0
    else:
     for i in range (0,num):
        r = r + 1 * i * i
        rs.AddCircle(pt, r)
        pt.Y = pt.Y + 1 
        pt.Z = pt.Z + 1 * i * 4 



 
 
 
pt = rs.GetPoint("Pick starting point")
num = rs.GetInteger("Enter a the number of iterations" )

Circles(pt, 1)
