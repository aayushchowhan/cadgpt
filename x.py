FREECADPATH = 'C:/Program Files/FreeCAD 0.20/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD , Part
import FreeCAD as App


import FreeCAD

# Create a new document
doc = FreeCAD.newDocument("Create_Cube")

# Create a cube
cube = FreeCAD.ActiveDocument.addObject("Part::Box","Cube")

# Set the cube's length, width, and height
cube.Length = 10
cube.Width = 10
cube.Height = 10

# Save the document
doc.saveAs("create_cube.FCStd")