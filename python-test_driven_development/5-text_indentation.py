#!/usr/bin/python3
'''
    A function that prints a text with 2 new lines;
        after each of these characters:
            ".", "?" and ":"
'''


def text_indentation(text):
    '''
        Args:
            text: The text to print(string).
        Raises:
            TypeError: If the text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        res = []
        a = 0
        text_lenght= len(text)
        space_skip = True
        is_end = False
        is_delim = False
        for i in range(text_lenght):
            is_end = i == text_lenght - 1
            is_delim = text[i] in '.?:'
            if is_delim or is_end:
                res.append(text[a: i + 1] + ('\n\n' * is_delim))
                space_skip = True
                a = i + 1
            elif text[i] in ' \t\r\v' and space_skip:
                a += 1
            elif text[i] == '\n':
                res.append(text[a: i + 1].rstrip() + '\n')
                a += 1
                space_skip = True
            else:
                if space_skip:
                    a = i
                space_skip = False
        print(''.join(res), end='')
