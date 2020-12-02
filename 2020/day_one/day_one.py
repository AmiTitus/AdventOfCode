import functools
with open('./input', 'r') as f:
    entries = f.read().splitlines()

entries = [int(x) for x in entries]
for x, y, z in itertools.combinations(entries, 3):
    if x + y + z == 2020:
        print(x * y * z)
        break
