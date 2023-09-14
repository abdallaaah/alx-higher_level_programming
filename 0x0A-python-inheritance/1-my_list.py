#!/usr/bin/python3
"""deinfe class that inherif list"""


class MyList(list):
    """ class inherit form list"""

    def print_sorted(self):
        """ print list in assending order"""
        print(sorted(self))
