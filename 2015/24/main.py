# https://adventofcode.com/2015/day/24
import os
from itertools import combinations
from math import prod

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def package_weights(text: str) -> list[int]:
    return [int(line.strip()) for line in text.strip().splitlines() if line.strip()]


def min_quantum_entanglement(weights: list[int], groups: int) -> int:
    total = sum(weights)
    assert total % groups == 0

    target = total // groups
    n = len(weights)

    for r in range(1, n):
        candidates: list[tuple[int, ...]] = []
        for idxs in combinations(range(n), r):
            if sum(weights[i] for i in idxs) == target:
                candidates.append(idxs)
        if candidates:
            return min(prod(weights[i] for i in idxs) for idxs in candidates)

    raise ValueError("no partition")


def p1(text: str) -> int:
    return min_quantum_entanglement(package_weights(text), 3)


def p2(text: str) -> int:
    return min_quantum_entanglement(package_weights(text), 4)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
