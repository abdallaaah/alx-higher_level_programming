#!/usr/bin/python3
""" unitest function"""


def text_indentation(text):
    """ add indentation at the end of the line"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in punctuation_chars:
            result += "\n\n"

        i += 1

    print(result.strip())
