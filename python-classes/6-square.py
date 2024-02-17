#!/usr/bin/python3

# Clase Square que define un cuadrado
class Square:
    '''
    Clase Square que define un cuadrado.

    Atributos:
        __size (int): tamaño del cuadrado.

    Métodos:
        __init__: inicializa un objeto Square.
        size: obtiene y establece el tamaño del cuadrado.
        area: calcula el área del cuadrado.
    '''

    def __init__(self, size=0):
        '''
        Inicializa un objeto Square.

        Args:
            size (int): tamaño del cuadrado. (predeterminado: 0)

        Raises:
            TypeError: si size no es un entero.
            ValueError: si size es menor que 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size

    @property
    def size(self):
        '''
        Obtiene el tamaño del cuadrado.

        Returns:
            int: el tamaño del cuadrado.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Establece el tamaño del cuadrado.

        Args:
            value (int): el nuevo tamaño del cuadrado.

        Raises:
            TypeError: si value no es un entero.
            ValueError: si value es menor que 0.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        '''
        Calcula el área del cuadrado.

        Returns:
            int: el área del cuadrado.
        '''
        return self.__size * self.__size
