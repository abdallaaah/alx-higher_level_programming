#!/usr/bin/python3
def element_at(my_list, idx):
    """elemnt at to retrive the index"""
    if idx < 0 or idx >= (len(my_list)):
        return None
    else:
        return int(my_list[idx])
