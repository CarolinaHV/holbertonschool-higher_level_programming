#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    z = set_1.symmetric_difference(set_2)
    if z != diff:
        diff = (list(z))
    return diff
