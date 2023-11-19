class Rectangle:
    static_num = 0

    def __init__(self, lenght, breadth):
        Rectangle.static_num+=1
        self.length = lenght
        self.breadth = breadth

    def getLenght(self):
        return self.length

    def setLength(self,l):
        self.length = l

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def are(self):
        return self.length * self.breadth
    
    @classmethod # put the class as the first argument 
    def countRect(cls):
        print(cls.static_num)

    @staticmethod
    def issqueare(len, bre):
        return len==bre
      
r1 = Rectangle(15,25)
r2 = Rectangle(5,10)

Rectangle.countRect()
print(Rectangle.issqueare(10,10))