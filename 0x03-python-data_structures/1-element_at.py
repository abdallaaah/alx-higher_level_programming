#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """elemnt at to retrive the index"""
    if idx < 0 or idx >= (len(my_list)):
        return None
    else:
        return int(my_list[idx])
