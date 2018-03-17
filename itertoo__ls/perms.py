from itertools import permutations


def string_pers(string):
    per_m = [''.join(s) for s in permutations(string)]
    # return per_m[int(len(per_m)/2)]
    print(len(per_m))
    return per_m

print(string_pers('HACK'))

