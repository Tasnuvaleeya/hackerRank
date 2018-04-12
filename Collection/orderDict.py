from collections import OrderedDict
d= OrderedDict()
for _ in range(int(input())):
    item,price=input().rsplit(' ', 1)
    if item not in d:
        d[item]=int(price)
    else:
        d[item] = d[item] + int(price)
for i in d.items():
    print(*i)
#
# s = '----a---b--c-'
# print(s.rsplit())
# print(s.rsplit('-',1))
# print(s.rsplit('-',2))
# print(s.rsplit('-',4))