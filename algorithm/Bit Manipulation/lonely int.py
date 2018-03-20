#!/bin/python3

import sys

def lonelyinteger(a):
    # Complete this function
    for i in a:
        if len(a)==1:
            return i
        else:
            if a.count(i) == 1:
                return i
            # print(a.count(i), end=" ")

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
