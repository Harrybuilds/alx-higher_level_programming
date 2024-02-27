#!/usr/bin/python3

"""
module to house a class called Rectangle
inheriting from the base class Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from
    the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        rec = ''
        for j in range(self.y):
            print()
        for i in range(self.height):
            if i != self.height - 1:
                rec += '{} {}\n'.format(' ' * self.x, '#' * self.width)
            else:
                rec += '{} {}'.format(' ' * self.x, '#' * self.width)
        print(rec)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for ind, arg in enumerate(args):
                setattr(self, attrs[ind], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {'y': self.y, 'x': self.x, 'id': self.id, 'width': self.width, 'height': self.height}
