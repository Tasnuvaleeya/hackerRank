import numpy
n= list(map(float,input().split()))
m= int(input())

arr = numpy.array(n)
print(numpy.polyval(arr,m))
