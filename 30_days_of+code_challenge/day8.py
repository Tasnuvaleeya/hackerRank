N=int(input())
my_input = [input().split() for _ in range(N)]
phonebook = {k:v for k,v in my_input}

while True:
    try:
        name=input()
        if name in phonebook:
            print("%s = %s" %(name, phonebook[name]))
        else:
            print("Not found")
    except:
        break


