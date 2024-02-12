#!/usr/bin/python3
"""This contains the rectangle class"""
from .base import Base


class Rectangle(Base):
    """This rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the value of the width"""
        return self.__width

    @property
    def height(self):
        """Return the value of the height"""
        return self.__height

    @property
    def x(self):
        """Return the value of x"""
        return self.__x

    @property
    def y(self):
        """Return the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the value of the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with character #"""
        for y in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns key/value arguments to attributes"""

        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    self.id = arg
                elif ar == 1:
                    self.__width = arg
                elif ar == 2:
                    self.__height = arg
                elif ar == 3:
                    self.__x = arg
                elif ar == 4:
                    self.__y = arg
                ar += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""

        rect_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return rect_dict

    pass
