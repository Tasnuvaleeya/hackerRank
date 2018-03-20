# from functools import reduce
#
# result=reduce(lambda x,y: x+y,[1,2,3])
# print(result)
#
# from math import gcd
#
# res = reduce(gcd, [2,4,8],3)
# print(res)
#
from functools import reduce
from fractions import Fraction
def product(fracs):
    t = reduce(lambda x,y: x*y, fracs)
    return t.numerator, t.denominator

print(product([Fraction(1, 2), Fraction(3, 4), Fraction(5, 3)]))