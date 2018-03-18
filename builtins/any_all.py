
# if all(int(i)>0 for i in m):
#     if any(j==j[::-1] for j in m):
#         print('True')
#     else:
#         print('False')
# else:
#     print('False')
N = int(input())
m = input().split()
print(all(int(i)>0 for i in m) and any(j==j[::-1] for j in m))