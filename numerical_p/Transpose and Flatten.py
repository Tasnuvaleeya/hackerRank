import numpy

N,M = map(int, input().split())
arr = numpy.array([input().split() for _ in range(N)],int)
print(numpy.transpose(arr), arr.flatten(), sep='\n')