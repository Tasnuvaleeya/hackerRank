import numpy
m= int(input())
arr = numpy.array([input().split() for _ in range(m)],float)
print(numpy.linalg.det(arr))


