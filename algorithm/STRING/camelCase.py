#!/bin/python3

import sys

def camelcase(s):
    # Complete this function
    n=0
    for i in s.strip():
        if i.isupper():
            n += 1
    return n+1

    # return n
# print(camelcase(''))

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)