import itertools
from typing import List, Dict
from collections import Counter

with open('input') as f:
    entries = f.read()
entries: List[int] = [*map(int, entries.splitlines())]

def find_joltage(data: List[int]):
    adapters: List[int] = sorted(data)
    adapters.append(max(adapters) + 3)
    diffs: Dict[int, int] = {0: 0, 1: 0, 3: 0}
    jolt: int = 0
    for adapter in adapters:
        diffs[adapter - jolt] += 1
        jolt = adapter
    return diffs[1] * diffs[3]

joltage = find_joltage(entries)
print(joltage)

def find_combinations(data: List[int]):
    adapters = sorted(data)
    adapters.append(max(adapters) + 3)
    counter = Counter()
    counter[0] = 1
    for adapter in adapters:
        counter[adapter] = counter[adapter - 1] + counter[adapter - 2] + counter[adapter - 3]
    return counter[adapters[-1]]

print(find_combinations(entries))