#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

test_inp = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

true_inp = Path('inp_1').read_text()


def solve_1(inp: str) -> int:
    acc = 0
    cursor = 50
    for line in inp.splitlines():
        op = line[0]
        amt = int(line[1:])
        match op:
            case 'L':
                cursor = (cursor - amt) % 100
            case 'R':
                cursor = (cursor + amt) % 100
        if cursor == 0:
            acc += 1
    return acc


def solve_2(inp: str) -> int:
    acc = 0
    cursor = 50
    for line in inp.splitlines():
        op = line[0]
        amt = int(line[1:])
        free = amt // 100
        acc += free
        amt = amt % 100
        match op:
            case 'L':
                if cursor - amt < 0 and cursor != 0:
                    acc += 1
                cursor = (cursor - amt) % 100
            case 'R':
                if cursor + amt > 100:
                    acc += 1
                cursor = (cursor + amt) % 100
        if cursor == 0:
            acc += 1
    return acc


assert solve_1(test_inp) == 3
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 6
print(f'{solve_2(true_inp) = }')
