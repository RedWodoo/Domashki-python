"""
program
"""
class Stadion():
    """
    program
    """
    def __init__(self,name,date,country,city,capacity):
        """
        program
        """
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity
    def description(self, text):
        """
        program
        """
        return f'{self.name} --- {text}'
    def nothing(self):
        """
        program
        """
Stadioninfo = Stadion('Central Stadion',1998,'Kazakhstan','Almaty',"3000")
print(Stadioninfo.name,Stadioninfo.city)
text_input = input('Give description: ')
print(Stadioninfo.description(text_input))
