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
