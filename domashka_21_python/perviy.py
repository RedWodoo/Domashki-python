"""
program
"""
class Device:
    """
    program
    """
    def __init__(self, name, power, price):
        """
        program
        """
        self.name = name
        self.power = power
        self.price = price

    def get_info(self):
        """
        program
        """
        return f"{self.name}, {self.power}W, {self.price}€"

    def get_power(self):
        """
        program
        """
        return self.power

    def get_price(self):
        """
        program
        """
        return self.price


class CoffeeMachine(Device):
    """
    program
    """

    def __init__(self, name, power, price, coffee_types, grinder_type):
        """
        program
        """
        super().__init__(name, power, price)
        self.coffee_types = coffee_types
        self.grinder_type = grinder_type

    def make_coffee(self, type, beans_amount):
        """
        program
        """
        # if type in self.coffee_types:
        return f"Making {type} coffee with {beans_amount}g beans"
        # else:
        #     return f"Sorry, we don't have {type} coffee"

    def grind_beans(self, beans_amount):
        """
        program
        """
        return f"Grinding {beans_amount}g beans with {self.grinder_type} grinder"


class Blender(Device):
    """
    program
    """
    def __init__(self, name, power, price, blending_modes):
        """
        program
        """
        super().__init__(name, power, price)
        self.blending_modes = blending_modes

    def blend(self, mode, ingredients):
        """
        program
        """
        # if mode in self.blending_modes:
        return f"Blending {', '.join(ingredients)} with {mode} mode"
        # else:
        #     return f"Sorry, we don't have {mode} blending mode"


class MeatGrinder(Device):
    """
    program
    """
    def __init__(self, name, power, price, cutting_modes):
        """
        program
        """
        super().__init__(name, power, price)
        self.cutting_modes = cutting_modes

    def grind_meat(self, mode, meat_amount):
        """
        program
        """
        # if mode in self.cutting_modes:
        return f"Grinding {meat_amount}g meat with {mode} mode"
        # else:
        #     return f"Sorry, we don't have {mode} cutting mode"

coffee_machine = CoffeeMachine("Nespresso", 1000, 200, ["espresso", "latte", "cappuccino"], "burr")
print(coffee_machine.get_info())
print(coffee_machine.make_coffee("espresso", 10))
print(coffee_machine.grind_beans(10))

blender = Blender("Blendtec", 1500, 300, ["smoothie", "milkshake", "soup"])
print(blender.get_info())
print(blender.blend("smoothie", ["banana", "apple", "orange"]))

meat_grinder = MeatGrinder("MeatMaster", 2000, 400, ["mince", "shred", "chop"])
print(meat_grinder.get_info())
print(meat_grinder.grind_meat("mince", 100))
