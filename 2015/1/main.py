# https://adventofcode.com/2015/day/1
import os
from typing import Optional

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def p1(text: str) -> int:
    return text.count("(") - text.count(")")


def p2(text: str) -> Optional[int]:
    floor = 0
    for i, ch in enumerate(text, start=1):
        if ch == "(":
            floor += 1
        elif ch == ")":
            floor -= 1
        if floor == -1:
            return i

    return None


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read().strip()

    print(p1(text))
    print(p2(text))
