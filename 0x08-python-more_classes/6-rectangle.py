#!/usr/bin/python3
"""
Module that a define rectangle
"""


class rectangle:
    """
    Rectangle Class

     Attributes:
        number_of_instances: number of instances of the class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        Returns:
            rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value: rectangle width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle
        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value: rectangle height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Prints the rectangle with #
        Returns:
            string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        Returns:
            string representation of the rectangle to recreate a new instance
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes an instance of Rectangle and decrements the instance counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
