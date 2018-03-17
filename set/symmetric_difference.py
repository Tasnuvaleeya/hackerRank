# def symmetric_difference(a):
#     res = a.split()
#     return map(int,res)
# print(symmetric_difference('5,4,3,2)

#
# myset={1,2,3,4}
# myset1 ={3,4,5,6}
# myset2={2,4,6,7}
# print(myset.symmetric_difference(myset1))

#
# def symmetric_dif(M,N):
#     [print(i) for i in sorted(M.symmetric_difference(N))]
#
# print(symmetric_dif({1, 2, 3, 4}, {2, 3, 4, 7, 8}))

def findNumber(arr,k):
    if k in arr:
        return "YES"
    else:
        return "NO"
print(findNumber([1,2,3,5,6,7],4))
