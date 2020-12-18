#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(list(a_dictionary)):
        print("{:s}: {:s}".format(k, str(a_dictionary[k])))
