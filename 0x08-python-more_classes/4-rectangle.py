#!/usr/bin/python3

"""module that houses a class Rectangle """


class Rectangle:
    """ a class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes all instances of this class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for the width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width property """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to calculate the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ method to calculate the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ method that decides what to be printed
        when print is called on an instance of this class """

        if self.width == 0 or self.height == 0:
            return ""
        else:
            rec = ""
            for i in range(self.height):
                rec += "{}".format('#' * self.width) + '\n'
            return rec

    def __repr__(self):
        """The python representation of what to be printed """
        return f"{self.__class__.__name__}({self.width}, {self.height})"
