#!/usr/bin/python3
'''This defines a base geometry class BaseGeometry.'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        '''Not implemented yet.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
            Validate a parameter as an integer.
            Args:
                @name: The name (str) of the parameter.
                @value: The parameter (integer) to validate.
            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is <= 0.
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
