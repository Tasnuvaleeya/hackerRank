#!/bin/python3

import sys

def runningTime(arr):
    result = 0
    # Complete this function
    for i in range(1,len(arr)):
        for y in range(i - 1, -1, -1):
            if int(arr[i]) < int(arr[y]):
                arr[i],arr[y] = arr[y],arr[i]
                i = y
                result = result+ 1
    return result

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
