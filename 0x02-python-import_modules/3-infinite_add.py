#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numbers = len(sys.argv)
    add = 0

    for i in sys.argv[1:]:
        add = add + int(i)
    print("{}".format(add))
