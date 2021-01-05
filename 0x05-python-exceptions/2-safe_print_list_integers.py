#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end='')
            num_print += 1
        except (TypeError, ValueError):
            continue
    print()
    return num_print
