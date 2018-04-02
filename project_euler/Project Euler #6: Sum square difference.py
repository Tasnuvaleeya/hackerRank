def find_dif(n):
    sum = 0
    s = 0
    for i in range(n + 1):
        sum += i ** 2
        s += i
        m = s * s
    x = sum - m
    return abs(x)
t = int(input().strip())
for a0 in range(t):
    s = int(input().strip())

result = find_dif(s)
print(result)