"""
program
"""
class Ship:
    """
    program
    """
    def __init__(self,name,mass) -> None:
        """
        program
        """
        self.name = name
        self.mass = mass

    def get_info(self):
        """
        program
        """
        return f'{self.name}, {self.mass}'

    def get_mass(self):
        """
        program
        """
        return  self.mass

class Frigate(Ship):
    """
    program
    """
    def __init__(self, name, mass ,gun_type) -> None:
        """
        program
        """
        super().__init__(name, mass)
        self.gun_type = gun_type

    def fire(self,target,mode):
        """
        program
        """
        return f'{self.name} sets target on {target} by {self.gun_type}with  {mode} mode.'

    def defend(self,method):
        """
        program
        """
        return f"{self.name} uses {method} defense method."

class Destroyer(Ship):
    """
    program
    """
    def __init__(self, name, mass, speed,gun_calibre) -> None:
        """
        program
        """
        super().__init__(name, mass)
        self.speed = speed
        self.gun_calibre = gun_calibre

    def  move(self,speed):
        """
        program
        """
        return f'{self.name} moves at a speed of {speed}.'

    def  shoot(self,gun_calibre):
        """
        program
        """
        return f'{self.name} shooting to the target with {gun_calibre} calibre'

class Cruiser(Ship):
    """
    program
    """
    def __init__(self, name, mass,zone,carrier_guard) -> None:
        """
        program
        """
        super().__init__(name, mass)
        self.zone = zone
        self.carrier_guard = carrier_guard

    def patrol(self,zone):
        """
        program
        """
        return f'{self.name} is in patrol zone {zone}.'

    def carrier_defense(self,carrier_guard):
        """
        program
        """
        return f"{self.name} has {carrier_guard} guarding against."
Frigate_ship = Frigate('Georgia','150 tone','machine guns')
print(Frigate_ship.get_info())
print(Frigate_ship.fire('Pirats','peaceful'))
print(Frigate_ship.defend('captivity'))
Destroyer_ship= Destroyer("Nevada",350,"200 knots","40mm")
print(Destroyer_ship.get_info())
print(Destroyer_ship.move("20kn"))
print(Destroyer_ship.shoot(Destroyer_ship.gun_calibre))
Cruiser_ship = Cruiser("Baltimore",700,'A','Aircraft carrier')
print(Cruiser_ship.patrol('ZONE A'))
print(Cruiser_ship.carrier_defense(Cruiser_ship.carrier_guard))
