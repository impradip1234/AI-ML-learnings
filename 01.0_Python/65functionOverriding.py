# Q4. Create a class shape with a method Area().
    # Create subclasses Circle, Rectangle and Triangle that override the area() method.

from math import pi
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return (1/2)*self.base*self.height

c1=Circle(2)
print(c1.area())