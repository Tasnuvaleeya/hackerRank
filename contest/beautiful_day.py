i,j,k = [int(x) for x in input().split()]
print(sum((int(abs(beautiful_day - int(str(beautiful_day)[::-1])) % k == 0) for beautiful_day in range(i, j + 1))))
