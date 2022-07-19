#!/usr/bin/python3
"""
Class Square: adds a square area method
"""


class Square:
    """class square define a square"""

    def __init__(self, size=0):
        """conditional statements for the size variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the square area"""
        return self.__size * self.__size
