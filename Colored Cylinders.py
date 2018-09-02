import rhinoscriptsyntax as rs
 
 
ptt = rs.GetPoint("Pick starting point")
def createColoredCylinder(x,y,z,r,g,b):
    currentColor = [r,g,b]
    rs.AddPoint(x,y,z)
    pt = (x,y,z)
    cr = rs.AddCylinder(pt, (x + y) / 4, 5) 
    rs.ObjectColor(cr, currentColor)
 

rs.EnableRedraw(False)
step = 10

 
for x in range(1,200, step):
    for y in range(1,200, step):
        for z in range(1,2,step):
            createColoredCylinder(x,y,z,x,y,z)
rs.Redraw()

