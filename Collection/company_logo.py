import collections
from collections import Counter, OrderedDict
from operator import itemgetter

if __name__ == '__main__':

    s= input().strip()

# my_dict = collections.Counter(sorted(s))
# y_order = OrderedDict(my_dict)
# print(y_order)
# l= my_list.most_common(3)
# print(*l)
# print(my_dict)

#
# # print(*l)
# for i in l:
#     print(*i)
# #     # print('%s : %d' %(i, my_dict[i]))


class OrderedCounter(Counter, OrderedDict):
    pass
[print(*i) for i in OrderedCounter(sorted(s)).most_common(3)]

