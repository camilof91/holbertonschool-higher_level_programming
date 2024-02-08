#!/usr/bin/python3
if __name__ == "__main__":
    # Ejecutar el archivo variable_load_5.py en un nuevo espacio de nombres
    namespace = {}
    with open("variable_load_5.py", "r") as file:
        exec(file.read(), namespace)
    # Imprimir el valor de la variable a
    print(namespace.get("a"))
