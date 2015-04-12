#--- Playing with vectors. Example 2
#---

from FreeCAD import Vector
from pyooml import *

#-- Create a frame in the origin
frame()

#-- Show a point
v = Vector(10,10,10)
p = point(v)
sv = svector(v).color("yellow")

#-- Show a cube
c = cube(v)
c.ice(80)

#-- New frame of reference
f2 = frame()
f2.translate(v)

#-- Another frame of reference
f3 = frame()
f3.rotx(30)
f3.translate(v)
f3.translate(10,0,0)
