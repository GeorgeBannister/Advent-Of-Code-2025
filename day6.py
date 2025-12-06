#!/usr/bin/env python3
from __future__ import annotations

from functools import reduce
from pathlib import Path

test_inp = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

true_inp = Path('inp_6').read_text()


def solve_1(inp: str) -> int:
    cols = [[int(x)] for x in inp.splitlines()[0].split()]

    for line in inp.splitlines()[1:-1]:
        for idx, val in enumerate(line.split()):
            cols[idx].append(int(val))
    acc = 0
    for idx, x in enumerate(inp.splitlines()[-1].split()):
        match x:
            case '+':
                acc += reduce(lambda a, b: a + b, cols[idx], 0)
            case '*':
                acc += reduce(lambda a, b: a * b, cols[idx], 1)
    return acc


def solve_2(inp: str) -> int:
    rows = inp.splitlines()
    n_cols = max(len(row) for row in rows)
    n_rows = len(rows)
    bucket_acc = []
    curr_op = ''
    acc = 0
    for x in range(n_cols):
        col = []
        found = False
        for y in range(n_rows):
            item = rows[y][x]
            if item in ('+', '*'):
                curr_op = item
                found = True
                continue
            if item != ' ':
                col.append(item)
                found = True

        if not found or x == (n_cols - 1):
            if x == (n_cols - 1):
                bucket_acc.append(col)
            nums = [int(reduce(lambda a, b: a + b, x)) for x in bucket_acc]
            bucket_acc = []
            match curr_op:
                case '+':
                    acc += reduce(lambda a, b: a + b, nums, 0)
                case '*':
                    while 0 in nums:
                        nums.remove(0)
                    acc += reduce(lambda a, b: a * b, nums, 1)
        elif col:
            bucket_acc.append(col)
    return acc


assert solve_1(test_inp) == 4277556
print(f'{solve_1(true_inp) = }')
assert solve_2(test_inp) == 3263827
print(f'{solve_2(true_inp) = }')
