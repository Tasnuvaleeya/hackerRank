from itertools import *

n = int(input())
s = input().split()
k= int(input())
comb = list(combinations(s, k))
# print(output)
# a = len(output)
# b= output[:-1]
# print(b)

find_comb_having_a = [i for i in comb if 'a' in i]
#
print(list(find_comb_having_a))
#
# for i in s[0:k]:
#     print(i)
# print(s.index('a'))
# ind = s.index('a')
# print(ind)
print((len(find_comb_having_a)/len(comb)))