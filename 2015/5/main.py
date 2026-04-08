# https://adventofcode.com/2015/day/5
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

_VOWELS = frozenset("aeiou")
_FORBIDDEN = ("ab", "cd", "pq", "xy")


def is_nice(s: str) -> bool:
    if sum(1 for c in s if c in _VOWELS) < 3:
        return False
    if not any(s[i] == s[i + 1] for i in range(len(s) - 1)):
        return False
    if any(bad in s for bad in _FORBIDDEN):
        return False
    return True


def p1(lines: list[str]) -> int:
    return sum(1 for line in lines if is_nice(line))


def _has_non_overlapping_pair(s: str) -> bool:
    for i in range(len(s) - 1):
        pair = s[i : i + 2]
        if pair in s[i + 2 :]:
            return True

    return False


def _has_skip_repeat(s: str) -> bool:
    return any(s[i] == s[i + 2] for i in range(len(s) - 2))


def is_nice_new(s: str) -> bool:
    return _has_non_overlapping_pair(s) and _has_skip_repeat(s)


def p2(lines: list[str]) -> int:
    return sum(1 for line in lines if is_nice_new(line))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    print(p1(lines))
    print(p2(lines))
