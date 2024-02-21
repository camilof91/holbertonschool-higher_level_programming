#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    '''
    Args:
    text: The text to print(string).
    Raises:
    TypeError: If the text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        res = []
        line = ""
        for char in text:
            line += char
            if char in ".?:":
                res.append(line.strip())
                res.append("\n\n")
                line = ""
        res.append(line.strip())  # Add the remaining text
        print("".join(res), end='')
