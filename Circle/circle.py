import math
class Circle:
    def __init__(self,radius = 1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,radius):
        if(radius<0):    
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    
    @property
    def diameter(self): 
        return self.radius*2
    @property
    def area(self):
        return math.pi*self.radius**2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2
        
    def __str__(self):
        return 'Circle({})'.format(self.radius)
    def __repr__(self):
        return 'Circle({})'.format(self.radius)

c = Circle(5)
print(c.radius)
print(c.diameter)
print(c.area)
c.diameter = 2
c = Circle()
print(c.radius)
print(c.diameter)
print(c.area)
c
