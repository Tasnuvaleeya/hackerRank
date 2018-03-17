import sys


def birthdayCakeCandles(ar):
    max_height = 0
    count = 0
    for i in ar:
        if i > max_height:
            max_height = i
    for j in ar:
        if j == max_height:
            count += 1
    return count
print(birthdayCakeCandles([1, 3, 2, 3, 3]))

# n = int(input().strip())
# ar = list(map(int, input().split(' ')))
# result = birthdayCakeCandles(n, ar)
# print(result)
