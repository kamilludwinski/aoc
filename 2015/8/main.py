# https://adventofcode.com/2015/day/8
import ast
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def p1(text: str) -> int:
    code_total = 0
    memory_total = 0

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        code_total += len(line)
        memory_total += len(ast.literal_eval(line))

    return code_total - memory_total


def _encode_literal(line: str) -> str:
    parts = ['"']

    for c in line:
        if c == "\\":
            parts.append("\\\\")
        elif c == '"':
            parts.append('\\"')
        else:
            parts.append(c)

    parts.append('"')

    return "".join(parts)


def p2(text: str) -> int:
    delta = 0

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        encoded = _encode_literal(line)
        delta += len(encoded) - len(line)

    return delta


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
