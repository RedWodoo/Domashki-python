class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if type(other) == Circle:
            return self.radius == other.radius
        return False

    def __gt__(self, other):
        if type(other) == Circle:
            return self.radius > other.radius
        return False

    def __lt__(self, other):
        if type(other) == Circle:
            return self.radius < other.radius
        return False

    def __ge__(self, other):
        if type(other) == Circle:
            return self.radius >= other.radius
        return False

    def __le__(self, other):
        if type(other) == Circle:
            return self.radius <= other.radius
        return False

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self
    
    def __str__(self):
        return f"{self.radius}"


c1 = Circle(5)
c2 = Circle(7)
c3 = Circle(5)

print(c1 == c2)     
print(c1 > c2)        
print(c1 < c2)        
print(c1 >= c2)      
print(c1 <= c2)       
print(c1 == c3)      
print(c1 + 2)   
print(c1 == c3)      