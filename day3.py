#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from itertools import combinations

if TYPE_CHECKING:
    from collections.abc import Generator

test_inp = """987654321111111
811111111111119
234234234234278
818181911112111"""

true_inp = Path('inp_3').read_text()


def solve_1(inp: str) -> int:
    acc = 0
    for bank in inp.splitlines():

        def opt(bank: str) -> Generator[int, None, None]:
            for i in range(len(bank)):
                for i2 in range(i + 1, len(bank)):
                    yield (int(f'{bank[i]}{bank[i2]}'))

        acc += max(opt(bank))
    return acc


def solve_2(inp: str) -> int:
    acc = 0
    for b in inp.splitlines():
        string_build = ''
        left_to_find = 12
        string_left = f'{b}'
        while left_to_find > 0:
            l = len(string_left)
            sub = string_left[: (-left_to_find + 1)]
            if left_to_find == 1:
                sub = string_left
            max_digit = max(int(x) for x in sub)
            for idx in range(len(sub)):
                if int(sub[idx]) == max_digit:
                    string_build += sub[idx]
                    string_left = string_left[idx + 1 :]
                    left_to_find -= 1
                    break
        acc += int(string_build)
    return acc


assert solve_1(test_inp) == 357
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 3121910778619
print(f'{solve_2(true_inp) = }')
