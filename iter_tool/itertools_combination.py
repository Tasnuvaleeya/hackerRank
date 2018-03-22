from itertools import *

string,i = input().split()
for i in range(1, int(i)+1):
    for s in combinations(sorted(string),i):
        print(''.join(s))
