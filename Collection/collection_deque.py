from collections import deque
d= deque()
for i in range(int(input())):
    s = input().split()
    getattr(d, s[0])(*s[1:])
print(' '.join(d))
