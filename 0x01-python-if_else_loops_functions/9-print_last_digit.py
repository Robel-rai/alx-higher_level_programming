#!/usr/bun/bash/python3
def print_last_digit(number):
    if number < 0:
        i = ((number * -1) % 10)
        return i
    else:
        i = (number % 10)
        return i
