#!/usr/bin/python3
"""Define a Square class with width and height attributes."""


class Square:
    """Represent a square with width and height attributes."""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize a Square object.

        Args:
            *args: Variable length argument list (unused).
            **kwargs: Arbitrary keyword arguments to set attributes.

        Attributes:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def permiter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Represent the square as a string."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create a Square object, print its details, area, and perimeter."""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
