# https://adventofcode.com/2015/day/25
import os
import re

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_MOD = 33_554_393
_MUL = 252_533
_START = 20_151_125

_POS = re.compile(r"row (\d+), column (\d+)")


def parse_target(text: str) -> tuple[int, int]:
    m = _POS.search(text)
    if not m:
        raise ValueError("expected 'row N, column M' in input")

    return int(m.group(1)), int(m.group(2))


def code_at(target_row: int, target_col: int) -> int:
    r, c = 1, 1
    x = _START
    while (r, c) != (target_row, target_col):
        x = (x * _MUL) % _MOD
        if r > 1:
            r -= 1
            c += 1
        else:
            r = c + 1
            c = 1
    return x


def p1(text: str) -> int:
    row, col = parse_target(text)
    return code_at(row, col)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
