import re
from typing import Dict


with open('input') as f:
    entries = f.read()
entries = entries.splitlines()

line_regex = re.compile(r'(?P<color>\w+ \w+) bags contain (?P<bags>[^\..]+)\.')
bags_regex = re.compile(r'(?P<number>\d+) (?P<color>\w+ \w+) bags?')

bags: Dict = dict()
for entry in entries:
    color, subline = line_regex.match(entry).groups()
    bags[color] = subbags = {}
    for count, subcolor in bags_regex.findall(subline):
        subbags[subcolor] = int(count)

def solve(color, only_colors=False, only_counts=False):
    colors = set()
    counts = 0
    for color, count in bags.get(color).items():
        subcolors, subcounts = solve(color)
        counts += count + (subcounts * count)
        colors.add(color)
        colors.update(subcolors)
    if only_colors:
        return colors
    if only_counts:
        return counts
    return colors, counts

print(sum('shiny gold' in solve(color, only_colors=True) for color in bags))
print(solve('shiny gold', only_counts=True))