from __future__ import annotations
from typing import List, Callable
from collections import Counter

Grid = List[List[str]]

neighbours = [(-1, 0), (-1, -1), (-1, +1), 
             ( 0,-1),           ( 0, +1),
             ( 1, 1), (1,  0),  (1, - 1)]

def next_value(grid: Grid, i: int, j: int) -> str:
    number_rows:int = len(grid)
    number_columns:int = len(grid[0])

    counts = Counter(
        grid[i + di][j + dj]
        for di, dj in neighbours
        if 0 <= i + di < number_rows and 0 <= j + dj < number_columns
    )

    c = grid[i][j]    

    if c == 'L' and counts['#'] == 0:
        return '#'
    if c == '#' and counts['#'] >= 4:
        return 'L'
    else:
        return c

def step(grid: Grid) -> Grid:
    return [
        [
            next_value(grid, i, j)
            for j, c in enumerate(row)
        ]
        for i, row in enumerate(grid)
    ]

def first_seat(grid: Grid, i: int, j: int, di: int, dj: int) -> str:
    nr = len(grid)
    nc = len(grid[0])

    while True:
        i += di
        j += dj

        if 0 <= i < nr and 0 <= j < nc:
            c = grid[i][j]
            if c == '#' or c == 'L':
                return c
        else:
            return '.'


def next_value2(grid: Grid, i: int, j: int) -> str:
    counts = Counter(
        first_seat(grid, i, j, di, dj)
        for di, dj in neighbours
    )

    c = grid[i][j]    

    if c == 'L' and counts['#'] == 0:
        return '#'
    if c == '#' and counts['#'] >= 5:
        return 'L'
    else:
        return c


def step2(grid: Grid) -> Grid:
    return [
        [
            next_value2(grid, i, j)
            for j, c in enumerate(row)
        ]
        for i, row in enumerate(grid)
    ]

def final_seats(grid: Grid, step_method: Callable) -> int:
    while (next_grid := step_method(grid)) != grid:
        grid = next_grid

    return sum(c == '#' for row in grid for c in row)

with open('input') as f:
    grid = [list(line.strip()) for line in f]

print(final_seats(grid, step))
print(final_seats(grid, step2))