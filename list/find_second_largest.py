# def find_second_max(arr):
#     x=arr.sort()
#     return list(x[::-1])
#
# print(find_second_max([1,2,3,4,5]))
# # my_list=[1,2,3,4,5]
# # print(my_list[::-1])
# #
# # if __name__ == '__main__':
# #     n = int(input())
# #     arr = map(int, input().split())
# #     print(arr[::-1])

x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans = [[i, j, k] for i in range(x+1) for j in range(y) for k in range(z) if i + j + k != n]
print(ans)