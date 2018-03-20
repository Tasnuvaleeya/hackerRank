cube = lambda x: x**3 # complete the lambda function

fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)

# print(list(map(lambda x: x**3, map(fib, range(int(input()))))))

out = list(map(fib, range(int(input()))))
print(list(map(cube, out)))
