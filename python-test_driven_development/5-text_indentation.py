#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    res = []
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            res.append(line.strip())
            res.append("\n\n")
            line = ""
    res.append(line.strip())
    print("".join(res), end='')
