# #!/bin/python3
#
# import sys
# import timeit
#
#
# fact_cache={}
# def factorial(n):
#     if n == 1:
#         return 1
#     if n==2:
#         return 2
#     if n>2:
#         return n * factorial(n-1)
# # print(factorial(3))

fact_cache ={}
def factorial(n):

    if n in [0, 1]:
        return n
    if n not in fact_cache:
        fact_cache[n] = n * factorial(n-1)
    return fact_cache[n]
# print(factorial(5))

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)


'''

# fact = lambda x: 1 if x<1 else x*fact(x-1)
# print(fact(int(input)))
#
# '''

import timeit
# fact = lambda x: 1 if x<1 else x*fact(x-1)
# print(fact(int(input())))
# print(timeit.timeit(fact))