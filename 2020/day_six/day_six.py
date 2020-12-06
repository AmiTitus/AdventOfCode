counts_part1:int = 0
counts_part2: int = 0
with open('input', 'r') as f:
    for line in f.read().split('\n\n'):
        lines = line.splitlines()
        counts_part1 += len(set(''.join(lines)))
        counts_part2 += len(set.intersection(*[set(l) for l in lines]))

print(f"Star 1 {counts_part1}")
print(f"Star 2 {counts_part2}")