#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return []
    unique = [0]
    res = 0
    for x in range(len(my_list)):
        if my_list[x] not in unique:
            res += my_list[x]
            unique.append(my_list[x])
        else:
            continue
    return res
