import re
T = int(input())
for _ in range(T):
    print(bool(re.match(r'^[-,+]?\d*\.\d+$', input())))
