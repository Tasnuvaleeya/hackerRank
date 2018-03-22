import numpy

n,m,p = map(int,(input().split()))

arr = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(m)], int)


print(numpy.concatenate((arr, arr2)))