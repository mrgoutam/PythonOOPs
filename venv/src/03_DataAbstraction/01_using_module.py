"""
Abstract class which has atleast one abstract method.
Abstract method is a method without implementation
"""

class Polygon:

    def noOfSides(self):
        pass

class Triangle(Polygon):

    def noOfSides(self):
        print("noOfSides: 3")

class Hexagon(Polygon):

    def noOfSides(self):
        print("noOfSides: 6")

r = Triangle()
r.noOfSides()

h = Hexagon()
h.noOfSides()