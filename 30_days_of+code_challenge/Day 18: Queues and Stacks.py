def is_palindrom(s):
    reversed_string=""
    for i in s:
        reversed_string = i+ reversed_string
    return reversed_string

print(is_palindrom('123'))
