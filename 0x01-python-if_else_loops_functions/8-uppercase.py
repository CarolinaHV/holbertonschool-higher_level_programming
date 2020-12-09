#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) in range(97, 124):
            rest = ord(letters) - 32
        else:
            rest = ord(letters)
        print("{:c}".format(rest), end="")
    print()
