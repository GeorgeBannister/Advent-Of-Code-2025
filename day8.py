#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from pathlib import Path

test_inp = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

true_inp = Path('inp_8').read_text()


@dataclass(frozen=True, slots=True)
class Co3:
    x: int
    y: int
    z: int

    def distance_to(self, other: Co3) -> int | float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5


def solve_1(inp: str, n_conns) -> int:
    junction_boxes: list[Co3] = [eval(f'Co3({line})') for line in inp.splitlines()]
    circuits: list[set[Co3]] = []

    direct_connections: set[tuple[Co3, Co3]] = set()
    distances = [(a, b, a.distance_to(b)) for a in junction_boxes for b in junction_boxes if a != b]
    distances.sort(key=lambda x: x[2])
    d_iter = iter(distances)

    for _ in range(n_conns):
        curr_a, curr_b, _ = next(d_iter)

        while (curr_a, curr_b) in direct_connections:
            curr_a, curr_b, _ = next(d_iter)

        curr_a_in_circuit = any(curr_a in x for x in circuits)
        curr_b_in_circuit = any(curr_b in x for x in circuits)

        direct_connections.add((curr_a, curr_b))
        direct_connections.add((curr_b, curr_a))

        n_circuits = len(circuits)
        if curr_a_in_circuit and curr_b_in_circuit:
            found = False
            for idx in range(n_circuits):
                if found:
                    break
                for idy in range(n_circuits):
                    if found:
                        break
                    if curr_a in circuits[idx] and curr_b in circuits[idy] and idx != idy:
                        circuits[idx] |= circuits[idy]
                        circuits[idy] = set()
                        found = True

        elif curr_a_in_circuit:
            for idx in range(n_circuits):
                if curr_a in circuits[idx]:
                    circuits[idx].add(curr_b)

        elif curr_b_in_circuit:
            for idx in range(n_circuits):
                if curr_b in circuits[idx]:
                    circuits[idx].add(curr_a)

        else:
            circuits.append({curr_a, curr_b})
    return reduce(lambda a, b: a * b, sorted([len(x) for x in circuits], reverse=True)[:3], 1)


def solve_2(inp: str) -> int:
    junction_boxes: list[Co3] = [eval(f'Co3({line})') for line in inp.splitlines()]
    circuits: list[set[Co3]] = []
    direct_connections: set[tuple[Co3, Co3]] = set()

    def is_solved() -> bool:
        return max(len(x) for x in circuits) == len(junction_boxes)

    distances = [(a, b, a.distance_to(b)) for a in junction_boxes for b in junction_boxes if a != b]
    distances.sort(key=lambda x: x[2])
    d_iter = iter(distances)

    while True:
        curr_a, curr_b, _ = next(d_iter)

        while (curr_a, curr_b) in direct_connections:
            curr_a, curr_b, _ = next(d_iter)

        curr_a_in_circuit = any(curr_a in x for x in circuits)
        curr_b_in_circuit = any(curr_b in x for x in circuits)

        direct_connections.add((curr_a, curr_b))
        direct_connections.add((curr_b, curr_a))

        n_circuits = len(circuits)

        if curr_a_in_circuit and curr_b_in_circuit:
            found = False
            for idx in range(n_circuits):
                if found:
                    break
                for idy in range(n_circuits):
                    if found:
                        break
                    if curr_a in circuits[idx] and curr_b in circuits[idy] and idx != idy:
                        circuits[idx] |= circuits[idy]
                        circuits[idy] = set()
                        if is_solved():
                            return curr_a.x * curr_b.x
                        found = True

        elif curr_a_in_circuit:
            for idx in range(n_circuits):
                if curr_a in circuits[idx]:
                    circuits[idx].add(curr_b)
                    if is_solved():
                        return curr_a.x * curr_b.x
        elif curr_b_in_circuit:
            for idx in range(n_circuits):
                if curr_b in circuits[idx]:
                    circuits[idx].add(curr_a)
                    if is_solved():
                        return curr_a.x * curr_b.x
        else:
            circuits.append({curr_a, curr_b})


assert solve_1(test_inp, 10) == 40
print(f'{solve_1(true_inp, 1000) = }')
assert solve_2(test_inp) == 25272
print(f'{solve_2(true_inp) = }')
