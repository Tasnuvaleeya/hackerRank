#!/bin/python3

import sys


n = int(input().strip())
for i in range(1,11):
    # print("{} * {} = {}".format(n, i, (n*i)))
    print(n, '*', i, '=', (n*i))
