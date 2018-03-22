from ITertools import permutations

n,i = input().split()
perm = [''.join(s) for s in permutations(sorted(n),int(i))]
print(*perm, sep="\n")

# def string_pers(n):
#     per_m = [''.join(s) for s in permutations(input(),2)]
#     print(len(per_m))
#     return per_m
#
# # print(string_pers('HACK'))
#
# result = string_pers(n)
# print(result)