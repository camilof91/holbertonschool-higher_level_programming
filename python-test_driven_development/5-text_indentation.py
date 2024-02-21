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
        if char in ".?:":
            # Check if the next character is a space:
            if len(text) > 1 and text[text.index(char) + 1].isspace():
                res.append(line.strip())
                res.append("\n\n")
                line = ""
    res.append(line.strip())  # Add the remaining text
    print("".join(res), end='')
