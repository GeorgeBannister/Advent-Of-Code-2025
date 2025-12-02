#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

test_inp = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

true_inp = Path('inp_2').read_text()


def solve_1(inp: str) -> int:
    acc = 0
    ranges: list[tuple[int, int]] = []
    for pair in inp.split(','):
        _l, _r = pair.split('-')
        left = int(_l)
        right = int(_r)
        ranges.append((left, right))
    biggest = max(x[1] for x in ranges)
    max_len = len(str(biggest)) // 2
    biggest_x = int('9' * max_len)
    for i in range(biggest_x):
        candidate = int(str(i) * 2)
        for bounds in ranges:
            if bounds[0] <= candidate <= bounds[1]:
                acc += candidate
    return acc


def solve_2(inp: str) -> int:
    acc = 0
    ranges: list[tuple[int, int]] = []
    for pair in inp.split(','):
        _l, _r = pair.split('-')
        left = int(_l)
        right = int(_r)
        ranges.append((left, right))
    biggest = max(x[1] for x in ranges)
    max_len = len(str(biggest)) // 2
    biggest_x = int('9' * max_len)

    found = set()

    for i in range(biggest_x):
        n = len(str(biggest)) // len(str(i))

        for mult in range(2, n + 1):
            candidate = int(str(i) * mult)
            for bounds in ranges:
                if bounds[0] <= candidate <= bounds[1] and candidate not in found:
                    acc += candidate
                    found.add(candidate)
    return acc


assert solve_1(test_inp) == 1227775554
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 4174379265
print(f'{solve_2(true_inp) = }')
