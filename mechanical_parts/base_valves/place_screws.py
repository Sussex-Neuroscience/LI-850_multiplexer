import os
nValves = 6
xDist = 11
yDist = 28
fileLoc = "C:\\Users\\Andre Maia Chagas\\Documents\\GitHub\\sussex\\LI700-multiplexer\\"
os.chdir(fileLoc)
#print(freecad.app.listDocuments(".\\"))

#doc = freecad.app.getDocument("test1.FCStd")
doc = App.newDocument("test")
base = doc.addObject("Part::Box","base")
base.Height = 5
base.Length = xDist+20
base.Width = nValves*yDist+10
vec1 = App.Vector(-10,-10,0)
base.Placement.Base = vec1
doc.recompute()
for i in range(nValves):#
	vec1 = App.Vector(0,i*yDist,-1)
	vec2 = App.Vector(xDist,i*yDist,-1)
	print(vec1)
	screw = doc.addObject("Part::Cylinder","screw"+str(i))
	screw.Radius = 1.65
	screw.Height = 10
	screw.Placement.Base = vec1
	screw = doc.addObject("Part::Cylinder","screw"+str(i))
	screw.Radius = 1.65
	screw.Height = 10
	screw.Placement.Base = vec2
doc.recompute()
