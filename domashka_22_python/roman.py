class Roman:
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    def __init__(self, numeral):
        self.numeral = numeral

    def __str__(self):
        return self.numeral

    def to_int(self):
        value = 0
        i = 0
        while i < len(self.numeral):
            if i + 1 < len(self.numeral) and self.numeral[i:i+2] in Roman.roman_numerals:
                value += Roman.roman_numerals[self.numeral[i:i+2]]
                i += 2
            else:
                value += Roman.roman_numerals[self.numeral[i]]
                i += 1
        return value

    def __add__(self, other):
        return Roman(str(self.to_int() + other.to_int()))

    def __sub__(self, other):
        return Roman(str(self.to_int() - other.to_int()))

    def __mul__(self, other):
        return Roman(str(self.to_int() * other.to_int()))

    def __truediv__(self, other):
        if other.to_int() == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Roman(str(self.to_int() // other.to_int()))

    
roman1 = Roman('XI')
roman2 = Roman('LV')


print(roman1 + roman2)  
print(roman1 - roman2)  
print(roman1 * roman2)  
print(roman1 / roman2)  