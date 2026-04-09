# https://adventofcode.com/2015/day/13
import os
import re
from itertools import permutations

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_LINE = re.compile(
    r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$"
)


def parse_happiness(text: str) -> dict[str, dict[str, int]]:
    h: dict[str, dict[str, int]] = {}
    for line in text.strip().splitlines():
        m = _LINE.match(line.strip())

        if not m:
            continue

        a, gl, n, b = m.group(1), m.group(2), int(m.group(3)), m.group(4)

        delta = n if gl == "gain" else -n
        h.setdefault(a, {})[b] = delta

    return h


def best_table_score(h: dict[str, dict[str, int]]) -> int:
    people = list(h.keys())

    n = len(people)
    best = float("-inf")

    for perm in permutations(people):
        total = 0
        for i in range(n):
            left = perm[i]
            right = perm[(i + 1) % n]
            total += h[left][right] + h[right][left]
        best = max(best, total)

    return int(best)


def p1(text: str) -> int:
    return best_table_score(parse_happiness(text))


def p2(text: str) -> int:
    h = parse_happiness(text)
    guests = list(h.keys())
    for p in guests:
        h[p]["You"] = 0

    h["You"] = {p: 0 for p in guests}

    return best_table_score(h)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
