"""
program
"""
class Car():
    """
    program
    """
    def __init__(self, name,publish,manufacturer,engine_vol,color,price):
        """
        program
        """
        self.name = name
        self.publish = publish
        self.manufacturer = manufacturer
        self.engine_vol = engine_vol
        self.color = color
        self.price = price
    def description(self, text):
        """
        program
        """
        return f'{self.name} --- {text}'
    def nothing(self):
        """
        program
        """
Audirs7 = Car('Audirs7',2023,'Volkswagen Group',4.0,"wet asphalt","100000$")
print(Audirs7.name)
text_input = input('Give description: ')
print(Audirs7.description(text_input))
