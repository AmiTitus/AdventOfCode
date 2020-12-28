import itertools
from typing import List, Set

with open('input') as f:
    entries = f.read()
entries = [int(x) for x in entries.splitlines()]

def find_error(data: List[int], preamble_size:int) -> List[int]:
    res: List[int] = []
    if len(data) <= preamble_size:
        return res
    preamble: List[int] = data[:preamble_size]
    combinations: Set = set(map(sum, itertools.combinations(preamble, 2)))
    value:int = data[preamble_size]
    if value not in combinations:
        res.append(value)
    return res + find_error(data[1:], preamble_size)

error = find_error(entries, 25)[0]
print(error)

def find_weakness(data: List[int], error: int):
    contiguous_values: List[int] = []
    for x in data:
        if x > error:
            break
        contiguous_values.append(x)
        while sum(contiguous_values) > error:
            contiguous_values.pop(0)
        if sum(contiguous_values) == error:
            return min(contiguous_values) + max(contiguous_values)

weakness = find_weakness(entries, error)
print(weakness)