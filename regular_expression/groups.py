import re
# m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
# n= re.match(r'(?P<user>(\w+))@(?P<website>(\w+))\.(?P<extension>(\w+))', 'username@hackerrank.com')
# print(m.group(0))
# print(m.group(1,2,3))
# print(m.groups())
# print(n.groupdict())

# s= input()
m = re.search(r'([a-zA-Z0-9])\1+', input())

print(m.group(1) if m else -1)