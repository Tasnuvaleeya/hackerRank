import re
s1 = input()
# s2 = input()
m= re.search(r'\d+', s1.index())
print(m.start())
print(m.end())