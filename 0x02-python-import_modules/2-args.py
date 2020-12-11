#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv)
    if number == 1:
        print("0 arguments.")
    elif number == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(number - 1))
    for i, argum in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, argum))
