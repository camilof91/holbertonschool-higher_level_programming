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

    listSearch = [".", "?", ":"]
    textIndent = ""
    prev_char = ''
    for char in text:
        if char == " " and prev_char == " ":
            continue
        textIndent += char
        if char in listSearch:
            textIndent += "\n\n"
        prev_char = char

    print(textIndent, end="")
