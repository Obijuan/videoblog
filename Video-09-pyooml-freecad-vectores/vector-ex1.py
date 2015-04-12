#--- Playing with vectors. Example 1
#---

from FreeCAD import Vector
from pyooml import *

#-- Create a vector (mathematical. Not shown)
v1 = Vector(30, 10, 0)

#-- Access to some properties
v1.x
v1.Length

#-- View the vector in 3D
sv1 = svector(v1)

#-- Create a second vector and show in 3D
v2 = Vector(10, 30, 0)
sv2 = svector(v2)

#-- Show the vector sum v1 + v2, in yellow
sv3 = svector(v1 + v2)
sv3.color("yellow")

#-- Show the typical paralelogram rule
sv2.translate(v1)

#-- Apply the cross product between v1 and v2
v4 = v1.cross(v2).normalize() * 10
sv4 = svector(v4).color("blue")

#-- Apply the cross product between v2 and v1
sv5 = svector( v2.cross(v1).normalize() * 10 )

#-- Calculate the difference between v4 and (v1 + v2)
sv6 = svector ( v4 - (v1 + v2)).color("green")
sv6.translate(v1 + v2)
