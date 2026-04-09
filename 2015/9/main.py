# https://adventofcode.com/2015/day/9
import os
import re
from collections import defaultdict
from itertools import permutations

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_LINE = re.compile(r"^(\w+) to (\w+) = (\d+)$")


def parse_distances(text: str) -> dict[str, dict[str, int]]:
    dist: dict[str, dict[str, int]] = defaultdict(dict)

    for line in text.strip().splitlines():
        m = _LINE.match(line.strip())

        if not m:
            continue

        a, b, d = m.group(1), m.group(2), int(m.group(3))

        dist[a][b] = d
        dist[b][a] = d

    return dist


def shortest_route_length(dist: dict[str, dict[str, int]]) -> int:
    cities = list(dist.keys())
    best = float("inf")

    for perm in permutations(cities):
        total = sum(dist[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
        best = min(best, total)

    return int(best)


def longest_route_length(dist: dict[str, dict[str, int]]) -> int:
    cities = list(dist.keys())
    best = 0

    for perm in permutations(cities):
        total = sum(dist[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
        best = max(best, total)

    return int(best)


def p1(text: str) -> int:
    return shortest_route_length(parse_distances(text))


def p2(text: str) -> int:
    return longest_route_length(parse_distances(text))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
