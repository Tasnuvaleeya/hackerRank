n=int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    my_input = input().split()
    if my_input[0] == 'pop':
        s.pop()
    if my_input[0] == 'remove':
        s.remove(int(my_input[1]))
    if my_input[0] == 'discard':
        s.discard(int(my_input[1]))
print(sum(s))
