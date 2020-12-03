from functools import partial, reduce

def trees_for_slope(g, slope):
    dx, dy = slope
    return sum(1 for y in range(0, len(g), dy) if g[y][int((dx * y / dy) % len(g[0]))] == '#')


def product(seq):
  return reduce(lambda a, b: a * b, seq)


with open('input') as f:
    grid = [l.rstrip() for l in f.readlines()]
print(trees_for_slope(grid, (3,1)))
print(product(map(partial(trees_for_slope, grid), [(1,1), (3,1), (5,1), (7,1), (1,2)])))
