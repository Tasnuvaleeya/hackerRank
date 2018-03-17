def my_num(n):
    return n[2:]
n= int(input().strip())
res = max(my_num(bin(n)).split('0')).count('1')
print(res)