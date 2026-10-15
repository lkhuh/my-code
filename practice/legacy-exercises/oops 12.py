from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self,alength,abreadth):
        self.length = alength
        self.breadth = abreadth

    def printarea(self):
        return self.length * self.breadth


h


rect1 = Rectangle()
print(rect1.printarea())

sqr = Square()
print(sqr.printarea())

