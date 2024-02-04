"""
program
"""
class Wheels:
    """Class representing a set of wheels with a given number of wheels."""

    def __init__(self, num_wheels):
        """
        Initialize a new Wheels object with the given number of wheels.

        :param num_wheels: The number of wheels.
        """
        self.num_wheels = num_wheels

    def rotate(self):
        """
        Rotate the wheels.

        :return: None
        """
        print(f"Rotating {self.num_wheels} wheels...")

    def empty(self):
        """
        prorgram
        """
        return 0

class Engine:
    """Class representing a car engine with a given horsepower."""

    def __init__(self, horsepower):
        """
        Initialize a new Engine object with the given horsepower.

        :param horsepower: The horsepower of the engine.
        """
        self.horsepower = horsepower

    def start(self):
        """
        Start the engine.

        :return: None
        """
        print(f"Starting engine with {self.horsepower} horsepower...")

    def empty(self):
        """
        prorgram
        """
        return 0

class Doors:
    """Class representing a set of doors with a given number of doors."""

    def __init__(self, num_doors):
        """
        Initialize a new Doors object with the given number of doors.

        :param num_doors: The number of doors.
        """
        self.num_doors = num_doors

    def open(self):
        """
        Open the doors.

        :return: None
        """
        print(f"Opening {self.num_doors} doors...")
    def empty(self):
        """
        prorgram
        """
        return 0

class Car(Wheels, Engine, Doors):
    """
    Class representing a car with a given number of wheels, horsepower, and doors.

    The car has a set of wheels, an engine, and a set of doors.
    """

    def __init__(self, num_wheels, horsepower, num_doors):
        """
        Initialize a new Car object with the given number of wheels, horsepower, and doors.

        :param num_wheels: The number of wheels.
        :param horsepower: The horsepower of the engine.
        :param num_doors: The number of doors.
        """
        Wheels.__init__(self, num_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, num_doors)
    def empty(self):
        """
        prorgram
        """
        return 0

car = Car(4, 200, 2)
car.rotate()
car.start()
car.open()
