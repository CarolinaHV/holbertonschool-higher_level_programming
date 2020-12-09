#!/usr/bin/python3
for num_one in range(9):
    for num_two in range(1, 10):
        if num_one < num_two:
            if num_one == 8 and num_two == 9:
                print("{}{}".format(num_one, num_two))
            else:
                print("{}{}, ".format(num_one, num_two), end="")
