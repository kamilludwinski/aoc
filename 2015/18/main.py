# https://adventofcode.com/2015/day/18
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

STEPS = 100


def parse_grid(text: str) -> list[list[bool]]:
    return [
        [c == "#" for c in line.strip()]
        for line in text.strip().splitlines()
        if line.strip()
    ]


def neighbors_on(g: list[list[bool]], r: int, c: int) -> int:
    h, w = len(g), len(g[0])
    n = 0

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue

            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w and g[rr][cc]:
                n += 1

    return n


def step(g: list[list[bool]], corners_stuck: bool) -> list[list[bool]]:
    h, w = len(g), len(g[0])
    corners = {(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)}
    ng = [[False] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if corners_stuck and (r, c) in corners:
                ng[r][c] = True
                continue

            on = neighbors_on(g, r, c)
            if g[r][c]:
                ng[r][c] = on in (2, 3)
            else:
                ng[r][c] = on == 3

    return ng


def count_on_after(text: str, corners_stuck: bool) -> int:
    g = parse_grid(text)

    if corners_stuck:
        h, w = len(g), len(g[0])
        for r, c in ((0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)):
            g[r][c] = True

    for _ in range(STEPS):
        g = step(g, corners_stuck)

    return sum(sum(row) for row in g)


def p1(text: str) -> int:
    return count_on_after(text, corners_stuck=False)


def p2(text: str) -> int:
    return count_on_after(text, corners_stuck=True)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
