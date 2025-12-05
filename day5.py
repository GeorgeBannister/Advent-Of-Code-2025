#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

test_inp = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

true_inp = Path('inp_5').read_text()


def solve_1(inp: str) -> int:
    ranges_s, ings_s = inp.split('\n\n')
    ranges = [(int(row.split('-')[0]), int(row.split('-')[1])) for row in ranges_s.splitlines()]
    ings = [int(x) for x in ings_s.splitlines()]
    acc = 0
    for ing in ings:
        found = False
        for r in ranges:
            if found:
                continue
            if r[0] <= ing <= r[1]:
                acc += 1
                found = True
    return acc


def solve_2(inp: str) -> int:
    ranges_s, _ = inp.split('\n\n')
    ranges = [[int(row.split('-')[0]), int(row.split('-')[1])] for row in ranges_s.splitlines()]
    changed = True
    while changed:
        changed = False

        for i1 in range(len(ranges)):
            if changed:
                break
            for i2 in range(len(ranges)):
                if changed:
                    break
                if i1 == i2:
                    continue
                v1 = ranges[i1]
                v2 = ranges[i2]
                if v1[0] <= v2[0] <= v1[1]:
                    if v1[0] <= v2[1] <= v1[1]:
                        ranges.pop(i2)
                        changed = True
                        break
                    if v2[1] > v1[1]:
                        ranges[i1][1] = v2[1]
                        ranges.pop(i2)
                        changed = True
                        break
                if v1[0] <= v2[1] <= v1[1]:
                    if v1[0] <= v2[0] <= v1[1]:
                        ranges.pop(i2)
                        changed = True
                        break
                    if v2[0] < v1[0]:
                        ranges[i1][0] = v2[0]
                        ranges.pop(i2)
                        changed = True
                        break
    return sum(r[1] - r[0] + 1 for r in ranges)


assert solve_1(test_inp) == 3
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 14
print(f'{solve_2(true_inp) = }')
