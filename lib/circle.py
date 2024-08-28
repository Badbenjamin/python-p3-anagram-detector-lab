import math

class Circle:
    def __init__(self, radius):
        self._radius = None

        self.radius = radius #this is set using the setter function


    # getter function
    @property
    def radius(self):
        # make sure getter refers to _radius
        return self._radius
    
    # setter function
    @radius.setter
    def radius(self, new_radius):
        if (isinstance(new_radius, int) or isinstance(new_radius, float)) and new_radius > 0:
            self._radius = new_radius
        else:
            print(f"radius must be a number greater than zero, not {new_radius}")

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, new_diameter):
        if (isinstance(new_diameter, int) or isinstance(new_diameter, float)) and new_diameter > 0:
            self.radius = new_diameter / 2
        else:
            print(f"diameter must be a number greater than zero, not {new_diameter}")
    
c1 = Circle(2)

c1.diameter = 8.5

print(c1.radius)