#!/usr/bin/python3
""""Define a class Base"""


class Base:
    __nb_objects = 0

    def __init__(self, id = None):
        """
        If the new object don't send a id 
        will be assigned one
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

"""if __name__ == "__main__":
    # Ejemplo de uso
    obj1 = Base()
    print(obj1.id)  # Salida: 1

    obj2 = Base()
    print(obj2.id)  # Salida: 2

    obj3 = Base(10)
    print(obj3.id) 

    obj4 = Base()
    print(obj4.id)"""

     