# https://adventofcode.com/2015/day/14
import os
import re
from dataclasses import dataclass

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_LINE = re.compile(
    r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$"
)

TIME_TOTAL = 2503


@dataclass(frozen=True)
class Reindeer:
    name: str
    speed: int
    fly: int
    rest: int


def parse_reindeer(text: str) -> list[Reindeer]:
    out: list[Reindeer] = []
    for line in text.strip().splitlines():
        m = _LINE.match(line.strip())
        if not m:
            continue

        out.append(
            Reindeer(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        )

    return out


def distance_at(r: Reindeer, t: int) -> int:
    cycle = r.fly + r.rest
    full, rem = divmod(t, cycle)
    dist = full * r.speed * r.fly
    dist += r.speed * min(rem, r.fly)

    return dist


def p1(text: str) -> int:
    deer = parse_reindeer(text)

    return max(distance_at(r, TIME_TOTAL) for r in deer)


def p2(text: str) -> int:
    deer = parse_reindeer(text)
    points = [0] * len(deer)

    for t in range(1, TIME_TOTAL + 1):
        dists = [distance_at(r, t) for r in deer]
        lead = max(dists)

        for i, d in enumerate(dists):
            if d == lead:
                points[i] += 1

    return max(points)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
