#------------------------------------------------------------------------------
#-- FRIKI:  Freecad, RobotIcs and KInematics
#------------------------------------------------------------------------------
#-- (C) Juan Gonzalez-Gomez (Obijuan)  March - 2015
#------------------------------------------------------------------------------
#-- Releases under the GNU GPL v2
#------------------------------------------------------------------------------

import FreeCAD
import Part
import math


#-- Draw a vector in the z axis
def vectorz(l = 10, l_arrow = 4, d = 1, mark = False, show = True):
	"""Draw a vector in the z axis. Parameters:
		 l : Lenght
         l_arrow: arrow length
		 d : vector diameter
	"""

	#-- Correct the length
	if (l < l_arrow):
		l_arrow = l/2

	vectz = Part.makeCylinder(d / 2.0, l - l_arrow)
	base = Part.makeSphere(d / 2.0)
	arrow = Part.makeCone(d/2 + 1, 0.2, l_arrow)
	arrow.Placement.Base.z = l - l_arrow

	#-- Create the union of all the parts
	union = vectz.fuse(base)
	union = union.fuse(arrow)

	#-- Return de vector z
	return union

def orientate(part, v, vref = FreeCAD.Vector(0, 0, 1)):

	#-- Special cases. Null vector. Ignore
	if v.Length == 0:
		return

	#-- Special case: Vector in the z axis, poiting to the negative
	if v.x == 0 and v.y==0 and v.z < 0:
		raxis = App.Vector(1, 0, 0)
	else:
		raxis = vref.cross(v)

	#-- Calculate the rotation angle (in degrees)
	angle = math.degrees(vref.getAngle(v))

	#-- Rotate vectz!
	part.Placement.Rotation = FreeCAD.Rotation(raxis, angle)

#-- Change the color to blue
def blue(part):
	part.ViewObject.ShapeColor = (0.0, 0.00, 1.00)

def red(part):
	part.ViewObject.ShapeColor = (1.0, 0.0, 0.0)

def green(part):
	part.ViewObject.ShapeColor = (0.0, 1.0, 0.0)

def gray(part):
	part.ViewObject.ShapeColor = (0.80,0.80,0.80)


def vector(x, y = None, z = None, l = None):

	#-- Function overloading. x is mandatory
	if y == None and z == None:
		#-- the first argument is an App.Vector
		v = x
	else:
		#-- The three components are given
		v = FreeCAD.Vector(x, y, z)

	#-- When length l is given, a vector with length = l and
	#-- orientation (x,y,z) is created
	if l == None:
		l = v.Length

	#-- Vector on the z axis
	vectz = vectorz(l = l)
	vref = FreeCAD.Vector(0, 0, 1)

	#------ Orientate vectz on the v direction
	#-- Calculate the rotation axis
	orientate(vectz, v)

	#-- Add the vector to the current document
	doc = FreeCAD.ActiveDocument
	vec = doc.addObject("Part::Feature","Vector")
	vec.Shape = vectz
	doc.recompute()

	#-- Change the vector visual properties
	vo = vec.ViewObject
	vo.DisplayMode="Shaded"

	return vec

def frame(l = 10):

	#-- Create the axes vectors with different colors
	x_axis = vector(1, 0, 0, l = l)
	x_axis.Label = "X_axis"
	red(x_axis)
	y_axis = vector(0, 1, 0, l = l)
	y_axis.Label = "Y_axis"
	green(y_axis)
	z_axis = vector(0, 0, 1, l = l)
	z_axis.Label = "Z_axis"
	blue(z_axis)

	#-- Origin
	doc = FreeCAD.ActiveDocument
	origin = doc.addObject("Part::Sphere","Origin")
	origin.Radius = 1

	#-- Make a compound
	f = doc.addObject("Part::Compound","Frame")
	f.Links = [x_axis, y_axis, z_axis, origin]
	f.ViewObject.DisplayMode = "Shaded"

	doc.recompute()
	return f

def point(x, y = None, z = None, d = 1.0):

	#-- Function overloading. x is mandatory
		#-- the first argument is an App.Vector
	if y == None and z == None:
		v = x
	else:
		#-- The three components are given
		v = FreeCAD.Vector(x, y, z)

	#-- The point is a sphere
	pp = Part.makeSphere(d / 2.0)

	#-- Add the point to the current document
	doc = FreeCAD.ActiveDocument
	p = doc.addObject("Part::Compound","Point")

	#-- Set the shape
	p.Shape = pp

	#-- Set the placement
	p.Placement.Base = v


	p.ViewObject.DisplayMode = "Shaded"
	doc.recompute()

	return p


print("Hola")
v = vector(10,10,10)
p = point(20, 20,20)
frame()
f = frame()

#-- Use a Matrix for changing the frame placement
M = FreeCAD.Matrix()
M.move(30, 0, 0)
f.Placement = FreeCAD.Placement(M)

#-- See the Current Matrix
f.Placement.toMatrix()


