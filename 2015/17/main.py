# https://adventofcode.com/2015/day/17
import os
from itertools import combinations

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

TARGET = 150


def container_sizes(text: str) -> list[int]:
    return [int(line.strip()) for line in text.strip().splitlines() if line.strip()]


def p1(text: str) -> int:
    sizes = container_sizes(text)
    n = len(sizes)
    count = 0

    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            if sum(sizes[i] for i in combo) == TARGET:
                count += 1

    return count


def p2(text: str) -> int:
    sizes = container_sizes(text)
    n = len(sizes)

    for r in range(1, n + 1):
        count = 0

        for combo in combinations(range(n), r):
            if sum(sizes[i] for i in combo) == TARGET:
                count += 1
        if count:
            return count

    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
