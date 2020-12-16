#!/usr/bin/python3
def no_c(my_string):
    w_list = list(my_string)
    for char in w_list:
        if char == 'C':
            w_list.remove('C')
        elif char == 'c':
            w_list.remove('c')
    new_list = ''.join(w_list)
    return(new_list)
