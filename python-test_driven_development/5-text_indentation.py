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
    def text_indentation(text):
        """
        Prints a text with 2 new lines after each of these characters: ., ? and :
        """
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        special_chars = [".", "?", ":"]
        result = ""
        line = ""
        for char in text:
            if char in special_chars:
                line += char
                result += line.strip() + "\n\n"
                line = ""
            else:
                line += char
        result += line.strip()
        print(result)
