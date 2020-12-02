import re
from collections import Counter
from typing import Tuple


pattern = re.compile(r"""-|:|\s""")

with open('./input.txt', 'r') as f:
    entries = [pattern.split(line.strip()) for line in f.readlines()]
def filter_entry_star1(e):
    cnt = Counter(e[-1])[e[2]] 
    return cnt >= int(e[0]) and cnt <= int(e[1])

def filter_entry_star2(e): 
    return bool(e[2] == e[-1][int(e[0]) - 1]) != bool(e[2] == e[-1][int(e[1]) - 1])

print(sum(map(lambda e: filter_entry_star1(e), entries)))

print(sum(map(lambda e: filter_entry_star2(e), entries)))
