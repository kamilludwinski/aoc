# https://adventofcode.com/2019/day/3
import os


def parse_wire(wire):
    x, y = 0, 0
    steps = 0
    points = {}
    for move in wire.split(","):
        d, n = move[0], int(move[1:])
        for _ in range(n):
            if d == "U":
                y += 1
            elif d == "D":
                y -= 1
            elif d == "L":
                x -= 1
            elif d == "R":
                x += 1
            steps += 1
            if (x, y) not in points:
                points[(x, y)] = steps
    return points


def p1(text: str) -> int:
    wire1, wire2 = text.strip().split("\n")
    points1 = set(parse_wire(wire1).keys())
    points2 = set(parse_wire(wire2).keys())
    crosses = points1 & points2
    return min(abs(x) + abs(y) for x, y in crosses)


def p2(text: str) -> int:
    wire1, wire2 = text.strip().split("\n")
    p1s = parse_wire(wire1)
    p2s = parse_wire(wire2)
    crosses = set(p1s.keys()) & set(p2s.keys())
    return min(p1s[pt] + p2s[pt] for pt in crosses)


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path, "r") as file:
        text = file.read().strip()
    print(p1(text))
    print(p2(text))
