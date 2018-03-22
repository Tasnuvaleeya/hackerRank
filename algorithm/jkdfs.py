import numerical_p
a= list(map(int, input().split()))
b= list(map(int, input().split()))

arr = numerical_p.array(a)
arr2 = numerical_p.array(b)
res = numerical_p.inner(arr, arr2)
res2 = numerical_p.outer(arr, arr2)
print(res)
print(res2)