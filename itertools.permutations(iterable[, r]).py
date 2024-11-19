from itertools import permutations
a, b = input().split()
vals = sorted(permutations(a, int(b)))
lst = list()
for val in vals:
    print("".join(val))
