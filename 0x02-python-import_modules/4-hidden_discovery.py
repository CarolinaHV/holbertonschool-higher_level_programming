#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for mod in dir(hidden_4):
        if mod[0] == '_' and mod[1] == '_':
            continue
        print(mod)
