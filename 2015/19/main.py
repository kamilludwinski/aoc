# https://adventofcode.com/2015/day/19
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def parse(text: str) -> tuple[list[tuple[str, str]], str]:
    rules: list[tuple[str, str]] = []
    molecule = ""

    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue

        if " => " in s:
            lhs, rhs = s.split(" => ", 1)
            rules.append((lhs.strip(), rhs.strip()))
        else:
            molecule = s

    return rules, molecule


def distinct_after_one(molecule: str, rules: list[tuple[str, str]]) -> int:
    seen: set[str] = set()
    for lhs, rhs in rules:
        start = 0

        while True:
            i = molecule.find(lhs, start)
            if i == -1:
                break

            seen.add(molecule[:i] + rhs + molecule[i + len(lhs) :])
            start = i + 1

    return len(seen)


def steps_to_e(molecule: str, rules: list[tuple[str, str]]) -> int:
    rev = [(b, a) for a, b in rules]
    rev.sort(key=lambda x: len(x[0]), reverse=True)
    steps = 0
    cur = molecule

    while cur != "e":
        for big, small in rev:
            if big in cur:
                cur = cur.replace(big, small, 1)
                steps += 1
                break
        else:
            raise RuntimeError("stuck reducing molecule; check rules / input")

    return steps


def p1(text: str) -> int:
    rules, mol = parse(text)

    return distinct_after_one(mol, rules)


def p2(text: str) -> int:
    rules, mol = parse(text)

    return steps_to_e(mol, rules)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
