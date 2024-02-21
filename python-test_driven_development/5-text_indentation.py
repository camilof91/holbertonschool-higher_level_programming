#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Return text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to process.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        result += text[c]
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                result += "\n\n"
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

    return result
