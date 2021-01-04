#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_print = 0
    for element in range (x):
        try:
            print(my_list[element], end='')
            num_print += 1
        except IndexError:
            break
    print()
    return num_print
