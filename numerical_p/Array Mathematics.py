import numpy
n,m = map(int, input().split())

arr = numpy.array([input().split() for _ in range(n)],int)
arr2 = numpy.array([input().split() for _ in range(n)],int)
print(numpy.add(arr,arr2), numpy.subtract(arr,arr2), numpy.multiply(arr,arr2),
      numpy.floor_divide(arr,arr2), numpy.mod(arr,arr2), numpy.power(arr,arr2),sep='\n')