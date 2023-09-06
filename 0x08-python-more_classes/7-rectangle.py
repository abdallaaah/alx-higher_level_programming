#!/usr/bin/python3
"""real rectangle class """


class Rectangle:
    """ class represent the rectange"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Create a new rectangel
        Args:
        width(int): width of rec
        height(int): height of rec
        """
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        rect = []
        if self.width == 0 or self.height == 0:
            return ""

        for i in range(self.height):
            for x in range(self.width):
                rect.append(self.print_symbol)
            if not i == self.height - 1:
                rect.append("\n")
        #print(rect)
        #return ''.join(rect)
        return ''.join(str(l) for l in rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return rect

    def __del__(self):
        """ print message in deleting """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
