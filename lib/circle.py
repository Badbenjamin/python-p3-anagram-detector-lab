import math

class Circle:
    def __init__(self, radius):
        self._radius = None

        self.radius = radius


    @property
    def radius(self):
        return self.radius
    
    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    
c1 = Circle(2)

print(c1.radius)