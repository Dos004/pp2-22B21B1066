def permutations(string):
    from itertools import permutations
    perm = [''.join(p) for p in permutations(string)] # ищет все возможные перестановки стринга
    return perm
print(permutations(str(input())))