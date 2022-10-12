#!/usr/bin/python3
"""
Module Square class with
inherits Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


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
