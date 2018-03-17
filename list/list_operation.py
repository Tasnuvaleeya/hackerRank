if __name__ == '__main__':
   N = int(input())

res = []
for _ in range(N):
    inp = input().split()
    print(inp)
    if inp[0] == 'print':
        print(res)
    else:
        if len(inp) == 1:
            eval("res.{}()".format(inp[0]))
        elif len(inp) == 2:
            eval("res.{}({})".format(inp[0], inp[1]))
        else:
            eval("res.{}({},{})".format(inp[0], inp[1], inp[2]))