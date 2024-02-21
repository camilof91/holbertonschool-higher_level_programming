#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    res = []
    line = ""
    for char in text:
        line += char
        if char in ".?:":  # Check if the character is a delimiter
            res.append(line.rstrip())  # Add the current line without trailing whitespace
            res.append("\n\n")  # Add two new lines after the delimiter
            line = ""  # Reset the line for the next iteration
    res.append(line.rstrip())  # Add the last line without trailing whitespace
    print("".join(res), end='')
