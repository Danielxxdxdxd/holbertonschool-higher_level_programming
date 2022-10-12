#!/usr/bin/python3
"""
Module BaseGeometry class
"""


class BaseGeometry:
    """Initization BaseGeometry"""

    def area(self):
        """
        Raises exeption with the message
        "area() is not implemented"
        """
        raise (Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        """
        Raise a TypeError, if value is not string
        Raise a ValueError, if value is less or equal 0
        """
        if type(value) is not int:
            raise (TypeError("{} must be an integer".format(name)))
        if value <= 0:
            raise (ValueError("{} must be greater than 0".format(name)))
