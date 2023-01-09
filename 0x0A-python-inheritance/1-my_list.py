#!/usr/bin/python3
"""Defined a class that inherits from list and pass to sort a list."""


class MyList(list):
    """ shoring algotithem using the sort function"""

    def print_sorted(self):
        """Print the sorted data in the assending format"""
        print(sorted(self))
