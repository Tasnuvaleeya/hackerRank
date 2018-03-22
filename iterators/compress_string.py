from itertools import groupby

groups = []
key = []
for k, g in groupby(input()):
    groups.append(list(g))
    key.append(k)

int_key = list(map(int,key))
find_len = [len(i) for i in groups]
zipped_out = tuple(zip(find_len,int_key))
print(*zipped_out)
