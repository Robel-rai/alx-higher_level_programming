#!/usr/bin/python3
""" Class for the base """


class Base:
    __nb_objects = 0
    """Base model.
    This Represents the "base" for all other classes in project 0x0C*.
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
