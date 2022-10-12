#!/usr/bin/python3
"""
Module Ractangle class with
inherits BaseGeometry
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
        Return area for a rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns size for a Rectangle with a message
        """
        size_msg = ("[Rectangle] {}/{}".format(self.__width, self.__height))
        return (size_msg)
