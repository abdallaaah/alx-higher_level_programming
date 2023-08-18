#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str:
        if i in 'abcdefghijklmnopqrstuvwqxyz':
            a = ord(i)
            b = a - 32
            output = output + chr(b)
        else:
            output = output + i
    print("{}".format(output))
