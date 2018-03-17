def icecreamParlor(m, arr):
    dict = {}
    for pos, spent_amount in enumerate(arr):
        if spent_amount in dict:
            return dict[spent_amount], pos + 1
        else:
            dict[m-spent_amount] = pos + 1

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print(" ".join(map(str, result)))
