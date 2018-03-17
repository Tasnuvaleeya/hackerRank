# from functools import lru_cache
# @lru_cache(maxsize=1000)
from functools import reduce
def aVeryBigSum(n, ar):
    sum = lambda x,y: x+y
    return reduce(sum,ar)

print(aVeryBigSum(6,(11100,111100,1002200,11134,1123,1567)))