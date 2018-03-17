def staircase(n):
    for i in range(n, 0, -1):
        print((i-1) * ' ' + ((n+1)-i) * '#')

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)


