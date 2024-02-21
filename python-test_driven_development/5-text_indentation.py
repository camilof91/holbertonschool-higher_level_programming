#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    line = ''

    for char in text:
        line += char
        if char in punctuations:
            lines.append(line.strip())
            lines.append('')
            line = ''

    if line or not lines:
        lines.append(line.strip())

    for i, line in enumerate(lines):
        if i % 2 == 0:
            print(line)
