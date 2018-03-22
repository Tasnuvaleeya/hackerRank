import numpy

n= list(map(float, input().split()))

arr = numpy.array(n)
print(numpy.floor(arr), numpy.ceil(arr),numpy.rint(arr), sep='\n')