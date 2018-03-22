from itertools import combinations_with_replacement

n,i = input().split()
res = [''.join(s) for s in combinations_with_replacement(sorted(n),int(i))]
print(*res, sep="\n")