N= int(input())
s= set(input().split())
n = int(input())
for _ in range(n):
    s1 = set(input().split())
    inp = input().split()

    if inp[0] == 'intersection_update':
        print(s.intersection_update(s1))
    elif inp[0] == 'update':
        print(s.update(s1))
    elif inp[0] == 'symmetric_difference_update':
        print(s.symmetric_difference_update(s1))
    else:
        print(s. difference_update(s1))
