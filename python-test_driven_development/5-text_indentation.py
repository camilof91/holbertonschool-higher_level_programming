#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''

def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    result = ''
    newline = True

    for char in text:
        if char == '.' or char == '?' or char == ':':
            result += char + '\n\n'
            newline = True
        elif char != ' ' and char != '\t' and char != '\n' and newline:
            result += char
            newline = False
        elif char != ' ' and char != '\t' and char != '\n' and not newline:
            result += ' ' + char
        elif char == ' ' and not newline:
            result += char

    return result
