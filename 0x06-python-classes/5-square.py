#!/usr/bin/python3
"""
Class Square: square class with conditional
statements
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
            self.size = size

    @property
    def size(self):
        """retrives the current private size attribute"""
        return self__size

    @size.setter
    def size(self, value):
        """set the size attribute value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print a square with # to stdout with the
        size attribute value"""
        if self.size != 0:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                    print("")
        else:
            print("")
