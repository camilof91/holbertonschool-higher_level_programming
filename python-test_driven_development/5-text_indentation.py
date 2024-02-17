#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # Iterate over each character in the text
    for char in text:
        # Print the character
        print(char, end='')

        # If the character is '.', '?', or ':', print 2 new lines
        if char in ('.', '?', ':'):
            print("\n\n", end='')
