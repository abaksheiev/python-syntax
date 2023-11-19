class Cuboid:
    def __init__(self,l,b,h):
        print(id(self))
        self.length=l
        self.breadth=b
        self.height=h
    
    def lidarea(self):
        return self.length * self.breadth
    
    def total(self):
        return 2 * (self.length * self.breadth +self.breadth*self.height+self.length*self.height )
    
    def volume(self):
        return self.length * self.breadth * self.height
    
        
c1 = Cuboid(10,5,3)
print('id(c1.volume)=', id(c1.volume))
print(c1.volume())

c2 = Cuboid(20,10,5)
print('id(c2.volume)=', id(c2.volume))
print(c2.volume())

c1.newProp = 'Prop99'
print(dir(c1))