class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price
    

    def __eq__(self, other):
        try:
            return self.area == other.area
        except AttributeError:
            return False
    

    def __ne__(self, other):
        try:
            return self.area != other.area
        except AttributeError:
            return True
    

    def __gt__(self, other):
        try:
            return self.price > other.price
        except AttributeError:
            return NotImplemented
    

    def __lt__(self, other):
        try:
            return self.price < other.price
        except AttributeError:
            return NotImplemented
    

    def __ge__(self, other):
        try:
            return self.price >= other.price
        except AttributeError:
            return NotImplemented
    

    def __le__(self, other):
        try:
            return self.price <= other.price
        except AttributeError:
            return NotImplemented
        
flat1 = Flat(50, 200000)
flat2 = Flat(60, 250000)


print(flat1 == flat2)


print(flat1 != flat2)  


print(flat1 > flat2) 

print(flat1 < flat2)  

print(flat1 >= flat2) 


print(flat1 <= flat2)  


print(flat1 > flat2)  


print(flat2 <= flat2)  