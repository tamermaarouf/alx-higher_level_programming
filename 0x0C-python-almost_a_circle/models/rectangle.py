#!/usr/bin/python3
'''Write the class Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constractor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, valueWidth):
        '''Setter'''
        self.integer_validator('width', valueWidth, False)
        self.__width = valueWidth

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, valueH):
        '''Setter'''
        self.integer_validator('height', valueH, False)
        self.__height = valueH

    @property
    def x(self):
        '''Getter'''
        return self.__x

    @x.setter
    def x(self, valueX):
        '''Setter'''
        self.integer_validator('x', valueX, True)
        self.__x = valueX

    @property
    def y(self):
        '''Getter'''
        return self.__y

    @y.setter
    def y(self, valueY):
        '''Setter'''
        self.integer_validator('y', valueY, True)
        self.__y = valueY

    def area(self):
        '''returns the area value of the Rectangle instance.'''
        return (self.__width * self.__height)

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        print((('\n' * self.__y) + (
            (' ' * self.__x) + '#' * self.__width + '\n') * self.__height),
              end='')

    def update(self, *args):
        '''that assigns an argument to each attribute:'''
        for arg in range(len(args)):
            match arg:
                case 0:
                    super().__init__(args[0])
                    continue
                case 1:
                    self.width = args[1]
                    continue
                case 2:
                    self.height = args[2]
                    continue
                case 3:
                    self.x = args[3]
                    continue
                case 4:
                    self.y = args[4]
                    break

    def integer_validator(self, name, value, eq):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if ((eq) and (value < 0)):
            raise ValueError('{} must be >= 0'.format(name))
        if ((not eq) and (value <= 0)):
            raise ValueError('{} must be > 0'.format(name))

    def __str__(self):
        '''returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height))
