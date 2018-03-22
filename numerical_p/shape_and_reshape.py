import numpy
# arr = input().strip().split(' ')
my_array = numpy.array(list(map(int, input().split())))
my_array.shape = (3, 3)
print(my_array)


"""

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    my_array = numpy.array(arr)
    my_array.shape = (3, 3)
    return my_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


"""