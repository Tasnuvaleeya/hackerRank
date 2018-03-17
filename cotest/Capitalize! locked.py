
# cap = ''.join([x.capitalize() for x in input().split(' ')])

# print(cap)

def cap_string(string):
    return ' '.join([x.capitalize() for x in string.split(' ')])
print(cap_string('1 w 2 r 3g'))