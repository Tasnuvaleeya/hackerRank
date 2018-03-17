# def list_operation(list,index,n):
def list_operation(array,i,e):
    list=[]
    list.insert(i,e)
    list.insert(i,e)
    list.insert(i,e)
    print(list)
    list.remove(e)
    list.append(e)
    list.append(e)
    list.sort()
    print(list)
    list.pop()
    list.reverse()
    print(list)
print(list_operation([],10,1))
print(list_operation([],6,1))


'''
list=[]
# print(list)
list.insert(0,5)
list.insert(1,10)
list.insert(0,6)
print(list)
list.remove(6)
list.append(9)
list.append(1)
list.sort()
print(list)
list.pop()
list.reverse()
print(list)
'''