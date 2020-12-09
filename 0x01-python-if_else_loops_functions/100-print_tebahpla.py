#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 == 0:
        rest = alpha
    else:
        rest = alpha - 32
    print("{:c}".format(rest), end="")
