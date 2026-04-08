# https://adventofcode.com/2015/day/6
import os
import re

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_INSTR = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")


def p1(text: str) -> int:
    grid = [[False] * 1000 for _ in range(1000)]

    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        m = _INSTR.match(line)

        if not m:
            raise ValueError(f"no match found: {line!r}")

        op, x1, y1, x2, y2 = m.group(1), *map(int, m.groups()[1:])
        xa, xb = min(x1, x2), max(x1, x2)
        ya, yb = min(y1, y2), max(y1, y2)

        for x in range(xa, xb + 1):
            row = grid[x]
            if op == "turn on":
                for y in range(ya, yb + 1):
                    row[y] = True
            elif op == "turn off":
                for y in range(ya, yb + 1):
                    row[y] = False
            else:
                for y in range(ya, yb + 1):
                    row[y] = not row[y]

    return sum(row.count(True) for row in grid)


def p2(text: str) -> int:
    grid = [[0] * 1000 for _ in range(1000)]

    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        m = _INSTR.match(line)

        if not m:
            raise ValueError(f"bad line: {line!r}")

        op, x1, y1, x2, y2 = m.group(1), *map(int, m.groups()[1:])
        xa, xb = min(x1, x2), max(x1, x2)
        ya, yb = min(y1, y2), max(y1, y2)

        for x in range(xa, xb + 1):
            row = grid[x]
            if op == "turn on":
                for y in range(ya, yb + 1):
                    row[y] += 1
            elif op == "turn off":
                for y in range(ya, yb + 1):
                    row[y] = max(0, row[y] - 1)
            else:
                for y in range(ya, yb + 1):
                    row[y] += 2

    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
