#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    """Print a square with the # character.

    Args:
        text (str): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    res = []
    line = ""
    for char in text:
        line += char
        if char in ".?:":  # Verifica si el carácter es un delimitador
            res.append(line.rstrip())  # Agrega la línea actual sin espacios en blanco al final
            res.append("\n\n")  # Agrega dos nuevas líneas después del delimitador
            line = ""  # Restablece la línea para la próxima iteración
    res.append(line.rstrip())  # Agrega la última línea sin espacios en blanco al final
    print("".join(res), end='')
