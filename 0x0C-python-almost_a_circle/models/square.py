#!/usr/bin/python3

"""
module that houses a class called Square
which inherits from another class called
Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that defines how a
    square is modelled. it inherits from
    the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        method to initialize a Square
        instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0. Example: width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'size': self.size, 'id': self.id}
