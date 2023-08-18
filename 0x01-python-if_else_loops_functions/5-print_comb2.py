#!/usr/bin/python3
for x in range(00, 100):
    if x < 99:
        print("{0:02d}".format(x), end=",")
    else:
        print("{}".format(x))
