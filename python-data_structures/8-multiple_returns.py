#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence:
        first_char = sentence[0]
        return (lenght, first_char)
    else:
        first_char = None
        return (lenght, first_char)
