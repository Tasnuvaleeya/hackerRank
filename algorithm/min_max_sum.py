import sys

def miniMaxSum(arr):
    sum = 0
    for i in arr:
        sum +=i
    print(sum-min(arr), sum-max(arr))
# print(miniMaxSum([1, 2,3,4,5]))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
