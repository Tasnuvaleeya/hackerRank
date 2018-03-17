#!/bin/python3

import sys
# from datetime import *
import timeit
def plusMinus(arr):
    # Complete this function
    ar_length = len(arr)

    pos_num = len([i for i in arr if i > 0])/ar_length
    neg_num = len([i for i in arr if i <0 ])/ar_length
    zero_is = len([i for i in arr if i == 0])/ar_length
    # print(timeit.timeit(pos_num))
    print(pos_num)
    print(neg_num)
    print(zero_is)

    # pos_num = [i for i in arr if i > 0]
    # neg_num = [i for i in arr if i < 0]
    # zero_is = [i for i in arr if i == 0]
    # print(len(pos_num)/ar_length)
    # print(len(neg_num)/ar_length)
    # print(len(zero_is)/ar_length)
    #
    # for i in arr:
    #     # print(i)
    #     if i < 0:
    #         ar.append(i)
    #     if i>0:
    #         ar2.append(i)
    #     if i==0:
    #         ar3.append(i)
    # print(len(ar2) / ar_length)
    # print(len(ar)/ar_length)
    # print(len(ar3)/ar_length)

# print(plusMinus([-4, 3, -9,0 ,4 ,1]))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)