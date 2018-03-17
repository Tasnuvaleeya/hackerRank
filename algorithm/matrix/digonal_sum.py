#!/bin/python3

import sys


def diagonalDifference(a):
    left_sum =0
    right_sum=0
    left_init=0
    right_init=-1
    for i in a:
        left_sum += i[left_init]
        left_init +=1
        right_sum +=i[right_init]
        right_init -=1
    return abs(left_sum - right_sum)


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)
