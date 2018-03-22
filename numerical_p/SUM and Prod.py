import numpy

n,m = map(int, input().split())
arr= numpy.array([input().split() for _ in range(n)],int)
sum_res = numpy.sum(arr,axis=0)

print(numpy.prod(sum_res,axis=0))