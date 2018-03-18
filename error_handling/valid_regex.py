import re
for _ in range(int(input())):
    try:
        a = input()
        re.compile(a)
        print(True)
    except re.error:
        print(False)