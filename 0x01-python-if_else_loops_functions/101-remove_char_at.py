#!/usr/bin/python3
def remove_char_at(str, n):
    i = len(str)
    for j in range (i):
        if j != n:
            print ("{}".format(str[j]), end="")
