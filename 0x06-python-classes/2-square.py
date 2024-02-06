#!/usr/bin/python3

class Square:
    """ a class that defines a square """

    def __init__(self, size=0):
        """ instantiates every object of this square class """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
