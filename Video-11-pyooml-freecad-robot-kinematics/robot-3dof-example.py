from FreeCAD import Vector
from pyooml import *
import HMatrix

#-- Create a new doc
doc = newdoc()

#-- Robot parameters
a1 = -30
a2 = -60
a3 = 70
L1 = 11
L2 = 40
L3 = 40

#--- Link vectors
v1 = Vector(0, 0, L1)
v2 = Vector(L2, 0, 0)
v3 = Vector(L3, 0, 0)

#--- Transformations
Ma = HMatrix.Rotz(a1) * HMatrix.Translation(v1)
Mb = HMatrix.Roty(a2)
Mc = HMatrix.Translation(v2)
Md = HMatrix.Roty(a3)
Me = HMatrix.Translation(v3)

#--- Graphical elements for the kinematics

f0 = frame()
f1 = frame()
f2 = frame()
f3 = frame()
#sv1 = svector(v1).color("yellow")
sv2 = svector(v2).color("yellow")
sv3 = svector(v3).color("yellow")

#--- Apply the transformations
f1.T = Ma
sv2.T = Ma * Mb
f2.T = Ma * Mb * Mc
sv3.T = Ma * Mb * Mc * Md
f3.T = Ma * Mb * Mc * Md * Me

#-- Create more graphical parts for the robot
base = cube(40, 40, 5, center = True).translate(0, 0, 5/2.).ice(80)
base2 = sphere(r = 14, angle1 = 0).translate(0, 0, 5).ice(80)
l2 = link(l = L2, D = 10, w = 5).ice(80)
l3 = link(l = L3, D = 10, w = 3).ice(80)

#-- Place the new parts
l2.T = Ma * Mb
l3.T = Ma * Mb * Mc * Md
