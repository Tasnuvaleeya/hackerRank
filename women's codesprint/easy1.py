#!/bin/python3

import os
import sys


#
# Complete the howMuchToAsk function below.
#
def howMuchToAsk(c, p):
    #
    # Return the amount the cashier should ask the customer or -1 if this exceeds 9.
    #
    output = (p - c)
    denom_list = [20, 50, 100, 500, 1000]

    min_val = min([abs(output-denom) for denom in denom_list])
    if output in denom_list:
        print(0)
    elif output < 9 and output != min_val:
        print(output)
    elif min_val > 9:
        print(-1)



if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        cp = input().split()

        c = int(cp[0])

        p = int(cp[1])

        result = howMuchToAsk(c, p)

    #     f.write(str(result) + '\n')
    #
    # f.close()

