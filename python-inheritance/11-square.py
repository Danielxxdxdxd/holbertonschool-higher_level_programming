#!/usr/bin/python3
"""
Module Square class with
inherits Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initization Rectangle"""

    def __init__(self, width, height):
        """
        width and height is a private instance
        Validation width and height must be
        positive integers
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return area for a object
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns size for a object with a message
        """
        size_msg = ("[{}] {}/{}".format(self.__class__.__name__,
                    self.__width, self.__height))
        return (size_msg)


class Square(Rectangle):
    """Initization Rectangle"""

    def __init__(self, size):
        """
        Size is a private instance
        Validation size must be
        positive integers
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)
