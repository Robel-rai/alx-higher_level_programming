#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_l = set(my_list)
    j = 0

    for i in uniq_l:
        j += i

    return (j)
