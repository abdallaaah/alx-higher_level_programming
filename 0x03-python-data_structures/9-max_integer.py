#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxx = -999
    for num in range(len(my_list)):
        if my_list[num] > maxx:
            maxx = my_list[num]
    return maxx
    
