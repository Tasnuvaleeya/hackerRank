import numpy
a= list(map(int, input().split()))
b= list(map(int, input().split()))

arr = numpy.array(a)
arr2 = numpy.array(b)
res = numpy.inner(arr,arr2)
res2 = numpy.outer(arr,arr2)
print(res)
print(res2)