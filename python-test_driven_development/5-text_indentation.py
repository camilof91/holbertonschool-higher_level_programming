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
        raise TypeError("text must be a string")
    for i, char in enumerate(text):
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
        elif char == ' ' and text[i-1] in (".", "?", ":"):
            pass
        else:
            print(char, end="")
