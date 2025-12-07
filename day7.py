#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

test_inp = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

true_inp = Path('inp_7').read_text()


@dataclass(frozen=True, slots=True)
class Coord:
    x: int
    y: int

    def __add__(self, other) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)


left = Coord(-1, 0)
right = Coord(1, 0)
down = Coord(0, 1)


class _Tachyon: ...


Tachyon = _Tachyon()


class _Splitter: ...


Splitter = _Splitter()


class CountedTachyon:
    def __init__(self):
        self.cnt = 1


def solve_1(inp: str) -> int:
    grid = {}
    lines = inp.splitlines()
    grid_height = len(lines)
    grid_width = len(lines[0])

    for idy, row in enumerate(lines):
        for idx, val in enumerate(row):
            if val == 'S':
                grid[Coord(idx, idy)] = Tachyon
            elif val == '^':
                grid[Coord(idx, idy)] = Splitter

    acc = 0
    for y in range(grid_height):
        for x in range(grid_width):
            candidate = Coord(x, y)
            if grid.get(candidate) is Tachyon:
                shadow = candidate + down
                if grid.get(shadow) is Splitter:
                    acc += 1
                    grid[shadow + left] = Tachyon
                    grid[shadow + right] = Tachyon
                elif grid.get(shadow) is None:
                    grid[shadow] = Tachyon
    return acc


def solve_2(inp: str) -> int:
    grid = {}
    lines = inp.splitlines()
    grid_height = len(lines)
    grid_width = len(lines[0])

    for idy, row in enumerate(lines):
        for idx, val in enumerate(row):
            if val == 'S':
                grid[Coord(idx, idy)] = CountedTachyon()
            elif val == '^':
                grid[Coord(idx, idy)] = Splitter

    def tachyonize(co: Coord, n: int) -> None:
        if isinstance(grid.get(co), CountedTachyon):
            grid[co].cnt += n
            return
        grid[co] = CountedTachyon()
        grid[co].cnt = n

    for y in range(grid_height):
        for x in range(grid_width):
            candidate = Coord(x, y)
            if isinstance(grid.get(candidate), CountedTachyon):
                current_tachyon: CountedTachyon = grid[candidate]
                shadow = candidate + down
                if grid.get(shadow) is Splitter:
                    tachyonize(shadow + left, current_tachyon.cnt)
                    tachyonize(shadow + right, current_tachyon.cnt)
                else:
                    tachyonize(shadow, current_tachyon.cnt)

    acc = 0
    for x in range(grid_width):
        candidate = Coord(x, grid_height - 1)
        if isinstance(grid.get(candidate), CountedTachyon):
            acc += grid[candidate].cnt
    return acc


assert solve_1(test_inp) == 21
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 40
print(f'{solve_2(true_inp) = }')
