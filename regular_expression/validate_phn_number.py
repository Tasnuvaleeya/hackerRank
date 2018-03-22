import re

N= int(input())
for _ in range(N):
    if re.match(r'[789]\d{9}$',input()):
        print('YES')
    else:
        print('NO')
