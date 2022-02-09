from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def no__of_sides(self):
        pass

class Triangle(Polygon):
    def no__of_sides(self):
        print("I have 3 sides")

class Quadrilateral(Polygon):
    def no__of_sides(self):
        print("I have 4 sides")

class Pentagon(Polygon):
    def no__of_sides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def no__of_sides(self):
        print("I have 6 sides")

tri = Triangle ()
quad = Quadrilateral ()
pen = Pentagon ()
hex = Hexagon ()

tri.no__of__sides ()
quad.no__of__sides ()
pen.no__of__sides ()
hex.no__of__sides ()
