# #!/bin/python3
#
# import sys
# import timeit
#
# def bigSorting(arr):
#     arr.sort(key=lambda x: (len(x),x))
#     print('\n'.join(arr))
# if __name__ == "__main__":
#     n = int(input().strip())
#     arr = []
#     arr_i = 0
#     for arr_i in range(n):
#        arr_t = str(input().strip())
#        arr.append(arr_t)
#     result = bigSorting(arr)
#
#     # print("\n".join(result))


n= int(input())
arr = [input() for _ in range(n)]
sort_arr = lambda x: (len(x),x)
arr.sort(key=sort_arr)
print('\n'.join(arr))