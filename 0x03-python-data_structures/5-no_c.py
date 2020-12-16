#!/usr/bin/python3
def no_c(my_string):
    w_list = list(my_string)
    new_list = ''
    for char in w_list:
        if char != 'C' and char != 'c':
            new_list += char
    return new_list
