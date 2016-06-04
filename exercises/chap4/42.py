#!/usr/bin/python

import string

def char_to_point(char):
    '''
    convert char to point
    '''

    chars = list(string.ascii_lowercase)

    if char not in chars:
        return 0
    else:
        return chars.index(char) + 1


words = ["attitude", "masturbation", "pussy", "discipline", "beer", "familug"]

points = [sum(char_to_point(char) for char in word) for word in words]

print(points)
