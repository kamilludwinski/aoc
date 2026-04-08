# https://adventofcode.com/2015/day/3
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


_DELTAS = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def p1(text: str) -> int:
    x = y = 0
    visited = {(x, y)}

    for ch in text.strip():
        if ch not in _DELTAS:
            continue

        dx, dy = _DELTAS[ch]
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)


def p2(text: str) -> int:
    sx = sy = rx = ry = 0
    visited = {(0, 0)}
    santa_turn = True

    for ch in text.strip():
        if ch not in _DELTAS:
            continue

        dx, dy = _DELTAS[ch]
        if santa_turn:
            sx += dx
            sy += dy
            visited.add((sx, sy))
        else:
            rx += dx
            ry += dy
            visited.add((rx, ry))
        santa_turn = not santa_turn

    return len(visited)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read().strip()

    print(p1(text))
    print(p2(text))
