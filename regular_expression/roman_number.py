import re

regex_pattern = r"(I|X|V|L|C|D|M)+"
print(str(bool(re.match(regex_pattern, input()))))
