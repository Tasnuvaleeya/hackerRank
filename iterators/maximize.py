from itertools import product

K,M = map(int,input().split())
n = (list(map(int, input().split()))[1:] for _ in range(K))
func = lambda x: sum(i**2 for i in x)%M
res = map(func, product(*n))
print(max(res))
