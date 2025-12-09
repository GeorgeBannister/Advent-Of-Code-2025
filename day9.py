#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

test_inp = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

true_inp = Path('inp_9').read_text()


@dataclass(frozen=True, slots=True)
class Co2:
    x: int
    y: int

    def area_with(self: Co2, other: Co2) -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


def solve_1(inp: str) -> int:
    coords = [eval(f'Co2({x})') for x in inp.splitlines()]
    return max(a.area_with(b) for a, b in combinations(coords, 2))


def solve_2(inp: str) -> int:
    return 0


assert solve_1(test_inp) == 50
print('Test 1 pass!')
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 24
print('Test 2 pass!')
print(f'{solve_2(true_inp) = }')
