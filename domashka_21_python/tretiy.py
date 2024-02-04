"""
program
"""
class Square:
    """Class representing a square with a top-left corner and side length."""

    def __init__(self,x1, y1,side):
        """
        Initialize a new Square object with the given top-left corner and side length.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param side: The length of the side of the square.
        """
        self.x1 = x1
        self.y1 = y1
        self.side = side

    def get_center(self):
        """
        Return the center coordinates of the square.

        :return: The x- and y-coordinates of the center of the square.
        """
        return self.x1 + self.side / 2, self.y1 + self.side / 2
    def empty(self):
        """
        prorgram
        """
        return 0

class Circle:
    """Class representing a circle with a center and radius."""

    def __init__(self, x, y, radius):
        """
        Initialize a new Circle object with the given center and radius.

        :param x: The x-coordinate of the center.
        :param y: The y-coordinate of the center.
        :param radius: The radius of the circle.
        """
        self.x = x
        self.y = y
        self.radius = radius

    def get_center(self):
        """
        Return the center coordinates of the circle.

        :return: The x- and y-coordinates of the center of the circle.
        """
        return self.x, self.y
    def empty(self):
        """
        prorgram
        """
        return 0

class CircleInSquare(Square, Circle):
    """
    Class representing a circle inscribed in a square.

    The circle is defined by the center coordinates and radius, and the square is
    defined by the top-left corner and side length.
    """

    def __init__(self, x, y, side):
        """
        Initialize a new CircleInSquare object with the given top-left corner and side length.

        The circle is inscribed in the square, so its radius is set to half the side length.

        :param x: The x-coordinate of the top-left corner of the square.
        :param y: The y-coordinate of the top-left corner of the square.
        :param side: The length of the side of the square.
        """
        Square.__init__(self, x, y, side)
        Circle.__init__(self, x + side / 2, y + side / 2, side / 2)
    def empty(self):
        """
        prorgram
        """
        return 0

cis = CircleInSquare(2, 2, 18)
print(f'Center: ({cis.x},{cis.y}), Radius:  {cis.radius}')
print(f'Top-left corner:  ({cis.x1}, {cis.y1}), Side length:  {cis.side}')
