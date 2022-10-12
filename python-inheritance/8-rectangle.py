#!/usr/bin/python3
"""
Module Ractangle class with
inherits BaseGemetry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initization Rectangle"""

    def __init__(self, width, height):
        """
        Width and height is a private instance
        Validation width and height must be
        positive integers
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
