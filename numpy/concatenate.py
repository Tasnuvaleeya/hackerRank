import numpy

m = list(map(int,(input().split())))
n = list(map(int, (input().split())))

arr = numpy.array(m)
arr2 = numpy.array(n)

print(numpy.concatenate((arr,arr2), axis=1))