import pyooml
import FreeCAD
import math
from pyooml import svector
from FreeCAD import Vector

#-- create a new document
doc = newdoc()

#-------------------- Vector field parameters
#-- Number of vectors
N = 20

#-- Radius
r = 20

#-------------- Calculate internal parameters
#-- Sector angle
ang = 360.0/N

#-- Initial radial vector
v1 = Vector(r, 0, 0)

#-- Radial vector rotated ang around z axis
vr = Vector(r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang)), 0)

#-- Vector difference. The one that will be displayed
vd = vr - v1

#----------------------- Create the field!
l = [svector(vd).translate(v1+Vector(4,0,0)).rotz(ang * i).color("red") for i in xrange(N)]
field = union(l)

#-- Show the section wire
cable = cylinder(r = 15, h = 50, center = True).color("green")

#-- Show the intensity vector (big and blue)
iv = svector((0,0,1), l = 150).translate(0,0,-150/2.).color("blue")
iv.d = 5
iv.arrow_l = 20

#---  Show the figure center and in axonometric view
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()