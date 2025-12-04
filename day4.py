#!/usr/bin/env python3
from __future__ import annotations

from itertools import combinations
from pathlib import Path
from typing import TYPE_CHECKING

from dataclasses import dataclass

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import Self

test_inp = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

type Coord = tuple[int, int]

true_inp = Path('inp_4').read_text()


class _Paper: ...


Paper = _Paper()


class _Empty: ...


Empty = _Empty()


def neighbours_of(co: Coord) -> Generator[Coord]:
    for a, b in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        yield (co[0] + a, co[1] + b)


def solve_1(inp: str) -> int:
    grid = {}
    acc = 0
    for y, row in enumerate(inp.splitlines()):
        for x, char in enumerate(row):
            if char == '@':
                grid[(x, y)] = Paper
            else:
                grid[(x, y)] = Empty

    for co, item in grid.items():
        if item is not Paper:
            continue
        n = 0
        for shadow in neighbours_of(co):
            if shadow in grid and grid[shadow] is Paper:
                n += 1
        if n < 4:
            acc += 1
    return acc


def solve_2(inp: str) -> int:
    grid = {}
    acc = 0
    for y, row in enumerate(inp.splitlines()):
        for x, char in enumerate(row):
            if char == '@':
                grid[(x, y)] = Paper
            else:
                grid[(x, y)] = Empty

    has_changed = True

    while has_changed:
        has_changed = False

        for co, item in grid.items():
            if item is not Paper:
                continue
            n = 0
            for shadow in neighbours_of(co):
                if shadow in grid and grid[shadow] is Paper:
                    n += 1
            if n < 4:
                acc += 1
                has_changed = True
                grid[co] = Empty
    return acc


assert solve_1(test_inp) == 13
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 43
print(f'{solve_2(true_inp) = }')
