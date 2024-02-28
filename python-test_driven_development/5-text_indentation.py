#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    listSearch = [".", "?", ":"]
    textIndent = ""
    copy = ''
    for chars in text:
        if chars not in listSearch:
            if copy == " " and chars == " ":
                continue
            if copy not in listSearch or chars != " ":
                textIndent += chars
            copy = chars
            continue
        copy = chars
        textIndent += chars
        textIndent += "\n" * 2
    print(textIndent, end="")
