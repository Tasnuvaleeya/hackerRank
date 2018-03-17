# n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])

hap = 0
for i in arr:
    if i in A:
        hap += 1
    if i in B:
        hap -= 1
print(hap)