#!/usr/bin/python3
def to_upper(character):
    if ord(character) >= 97 and ord(charcter) <= 122:
        return(ord(charcter) - 32)
    else:
        return ord(character)
    ::w
    def uppercase(string):
        string_new=""
        for character in string
        string_new += "%c"%to_upper(character)
        print("{:s}".format(string_new))
