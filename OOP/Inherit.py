class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
class Cuboid(Rectangle):
    def __init__(self, h, l, b):
        # Must be called explicitly
        super().__init__(l, b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height
    
r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())
print('---------')

c = Cuboid(3,10,15)
print(c.area())
print(c.perimeter())
print('Volumes is ', c.volume())

