n = int(input())
ints = input().split(' ')
t = tuple(int(i) for i in ints)
print(hash((t)))
