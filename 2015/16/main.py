# https://adventofcode.com/2015/day/16
import os
import re
from typing import Callable

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_TICKER: dict[str, int] = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

_SUE = re.compile(r"^Sue (\d+): (.+)$")


def parse_sue_line(line: str) -> tuple[int, dict[str, int]] | None:
    m = _SUE.match(line.strip())
    if not m:
        return None

    num = int(m.group(1))
    props: dict[str, int] = {}
    for part in m.group(2).split(", "):
        k, v = part.split(": ")
        props[k] = int(v)

    return num, props


def matches_part1(props: dict[str, int]) -> bool:
    for k, v in props.items():
        if _TICKER[k] != v:
            return False

    return True


def matches_part2(props: dict[str, int]) -> bool:
    for k, v in props.items():
        t = _TICKER[k]
        if k in ("cats", "trees"):
            if v <= t:
                return False
        elif k in ("pomeranians", "goldfish"):
            if v >= t:
                return False
        else:
            if t != v:
                return False

    return True


def find_sue(text: str, pred: Callable[[dict[str, int]], bool]) -> int:
    for line in text.strip().splitlines():
        parsed = parse_sue_line(line)
        if parsed is None:
            continue

        num, props = parsed
        if pred(props):
            return num

    raise ValueError("no matching Sue")


def p1(text: str) -> int:
    return find_sue(text, matches_part1)


def p2(text: str) -> int:
    return find_sue(text, matches_part2)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
