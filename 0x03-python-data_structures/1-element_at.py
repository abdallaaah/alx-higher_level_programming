#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= (len(my_list)):
        print("hello")
        return None
    else:
        return(int(my_list[idx]))
