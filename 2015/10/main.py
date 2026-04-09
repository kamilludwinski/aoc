# https://adventofcode.com/2015/day/10
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def look_say_step(s: str) -> str:
    i = 0
    parts: list[str] = []

    n = len(s)

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        parts.append(str(j - i))
        parts.append(s[i])

        i = j

    return "".join(parts)


def length_after_iterations(seed: str, steps: int) -> int:
    s = seed.strip()

    for _ in range(steps):
        s = look_say_step(s)

    return len(s)


def p1(text: str) -> int:
    return length_after_iterations(text, 40)


def p2(text: str) -> int:
    return length_after_iterations(text, 50)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
