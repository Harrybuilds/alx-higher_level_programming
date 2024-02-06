#!/usr/bin/python3

class Square:
    """ a class that defines a square """

    def __init__(self, size=0):
        """ instantiates every object of this square class """
        self.size = size


    @property
    def size(self):
        """ private instance attribute getter (__size)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ private instance attribute setter (__size) """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size =  value


    def area(self):
        """ computes and returns the area of the square object """        
        return self.size **2

