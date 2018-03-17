def findOdd(l,r):
    for i in range(l,r+1):
        if i%2!=0:
            print(i)

print(findOdd(2,9))