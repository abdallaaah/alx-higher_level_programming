#!/bin/usr/python3
def only_diff_elements(set_1, set_2):
    set_11 = list(set_1)
    set_22 = list(set_2)
    res = []
    for x in range(len(set_11)):
        if set_11[x] not in set_22:
            res.append(set_11[x])
    for y in range(len(set_22)):
        if set_22[y] not in set_11:
            res.append(set_22[y])
    return res
