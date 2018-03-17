#!/bin/python3

import sys

def super_reduced_string(s):

    for i in list(s):
        if s.count(i) % 2 == 0:

            s = s.replace(i, '')
            # print(s)
        return s


s = input().strip()
result = super_reduced_string(s)
print(result)
