# https://adventofcode.com/2019/day/4
import os
from collections import Counter


def parse_range(text: str) -> tuple[int, int]:
    start, end = text.strip().split("-")
    return int(start), int(end)

def valid(n: int) -> bool:
    s = str(n)
    return len(s) == 6 and any(s[i] == s[i+1] for i in range(5)) and all(s[i] <= s[i+1] for i in range(5))

def valid2(n: int) -> bool:
    s = str(n)
    c = Counter(s)
    return valid(n) and 2 in c.values()

def p1(text: str) -> int:
    start, end = parse_range(text)
    return sum(valid(n) for n in range(start, end + 1))

def p2(text: str) -> int:
    start, end = parse_range(text)
    return sum(valid2(n) for n in range(start, end + 1))

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path, "r") as file:
        text = file.read().strip()
    print(p1(text))
    print(p2(text))
