#!/usr/bin/python3

"""find peak of list of unsorted numbers"""


def find_peak(list_of_integers):
    """caller function"""
    loi = list_of_integers
    if loi is None or loi == []:
        return None

    return peak_help(loi, 0, len(loi) - 1)


def peak_help(loi, start, end):
    """helper function"""
    u = int((end - start)/2 + start)

    if u + 1 >= len(loi) or loi[u + 1] <= loi[u]:
        if u - 1 < 0 or loi[u - 1] <= loi[u]:
            return loi[u]
        else:
            return peak_help(loi, 0, u)
    else:
        return peak_help(loi, u + 1, end)
