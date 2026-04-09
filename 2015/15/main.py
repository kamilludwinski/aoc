# https://adventofcode.com/2015/day/15
import os
import re
from dataclasses import dataclass

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_LINE = re.compile(
    r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$"
)


@dataclass(frozen=True)
class Ingredient:
    cap: int
    dur: int
    fla: int
    tex: int
    cal: int


def parse_ingredients(text: str) -> list[Ingredient]:
    out: list[Ingredient] = []
    for line in text.strip().splitlines():
        m = _LINE.match(line.strip())

        if not m:
            continue

        out.append(
            Ingredient(
                int(m.group(2)),
                int(m.group(3)),
                int(m.group(4)),
                int(m.group(5)),
                int(m.group(6)),
            )
        )

    return out


def score_cookie(amounts: list[int], ing: list[Ingredient]) -> int:
    cap = dur = fla = tex = 0
    for a, i in zip(amounts, ing, strict=True):
        cap += a * i.cap
        dur += a * i.dur
        fla += a * i.fla
        tex += a * i.tex

    cap = max(0, cap)
    dur = max(0, dur)
    fla = max(0, fla)
    tex = max(0, tex)

    return cap * dur * fla * tex


def calories_total(amounts: list[int], ing: list[Ingredient]) -> int:
    return sum(a * i.cal for a, i in zip(amounts, ing, strict=True))


def partitions(n: int, k: int, prefix: list[int] | None = None) -> list[list[int]]:
    if prefix is None:
        prefix = []
    if k == 1:
        return [prefix + [n]]

    out: list[list[int]] = []

    for x in range(n + 1):
        out.extend(partitions(n - x, k - 1, prefix + [x]))

    return out


def p1(text: str) -> int:
    ing = parse_ingredients(text)
    k = len(ing)
    best = 0

    for amounts in partitions(100, k):
        best = max(best, score_cookie(amounts, ing))

    return best


def p2(text: str) -> int:
    ing = parse_ingredients(text)
    k = len(ing)
    best = 0
    for amounts in partitions(100, k):
        if calories_total(amounts, ing) != 500:
            continue

        best = max(best, score_cookie(amounts, ing))

    return best


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
