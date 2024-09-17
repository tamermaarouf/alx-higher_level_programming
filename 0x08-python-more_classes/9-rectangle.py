#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty class Rectangle that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ method is executed immediately after create an object """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return the rectangle perimeter """
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(str(
            self.print_symbol) * self.__width for _ in range(self.__height))

    def __repr__(self):
        """ a string representation of the rectangle to be able to recreate """
        return ('Rectangle({:d}, {:d})'.format(self.__width, self.__height))

    def __del__(self):
        """ when an instance of Rectangle is deleted """
        if self.number_of_instances > 0:
            print("Bye rectangle...")
            type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' that returns the biggest rectangle based on the area '''
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(width=size, height=size))
