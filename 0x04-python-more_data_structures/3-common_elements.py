#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = []
    set_11 = list(set_1)
    set_22 = list(set_2)
    for x in range(len(set_11)):
        temp = set_11[x]
        for y in range(len(set_22)):
            if set_22[y] == temp:
                res.append(temp)
                break
    return res
