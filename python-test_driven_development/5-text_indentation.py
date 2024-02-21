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
            lines.append(line.strip() + '\n\n')
            line = ''
    if line.strip():
        lines.append(line.strip())

    print('\n'.join(lines))
