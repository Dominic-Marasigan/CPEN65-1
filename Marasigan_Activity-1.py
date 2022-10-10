# Python program that computes for Area of a Circle given Radius and/or Diameter
# Area of Circle given Radius = (pi * r ** 2)
# Area of Circle given Diameter = (pi * d ** 2)/4

import math
class circle():
    def __init__(self, given):
        self.given = given

    def area_radius(self):
        return math.pi * (self.given ** 2)

    def area_diameter(self):
        return 0.25 * math.pi * (self.given ** 2)

rad = int(input("Enter radius of circle: "))
obj1 = circle(rad)
dia = int(input("\nEnter diamter of circle: "))
obj2 = circle(dia)
print("\nArea of Circle given Radius:", round(obj1.area_radius(), 2))
print("\nArea of Circle given Diameter:", round(obj2.area_diameter(), 2), "\n")