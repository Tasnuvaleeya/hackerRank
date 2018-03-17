# print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))

def average(array):
    # your code goes here
    return (sum(set(array)))/len(set((array)))
    # print(sum(array))

    # return len(set(array))

print(average([161,182,161,154,176,170,167,171,170,174]))