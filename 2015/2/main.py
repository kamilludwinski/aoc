# https://adventofcode.com/2015/day/2
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def wrapping_paper(l: int, w: int, h: int) -> int:
    a, b, c = l * w, w * h, h * l

    return 2 * (a + b + c) + min(a, b, c)


def ribbon(l: int, w: int, h: int) -> int:
    a, b, c = sorted((l, w, h))

    return 2 * (a + b) + l * w * h


def p1(text: str) -> int:
    total = 0
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        l, w, h = map(int, line.split("x"))
        total += wrapping_paper(l, w, h)

    return total


def p2(text: str) -> int:
    total = 0
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        l, w, h = map(int, line.split("x"))
        total += ribbon(l, w, h)

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
