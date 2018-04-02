import re
# N= int(input())


for _ in range(int(input())):
    string = input()
    pattern = re.compile(r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$')
    if re.match(pattern, string) and not re.search(r"([\d])\1\1\1", string.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
