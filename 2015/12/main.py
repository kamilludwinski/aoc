# https://adventofcode.com/2015/day/12
import json
import os
import re
from typing import Any

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def p1(text: str) -> int:
    return sum(int(m.group(0)) for m in re.finditer(r"-?\d+", text))


def sum_json_no_red(node: Any) -> int:
    if isinstance(node, int):
        return node
    if isinstance(node, str):
        return 0
    if isinstance(node, list):
        return sum(sum_json_no_red(x) for x in node)
    if isinstance(node, dict):
        if "red" in node.values():
            return 0

        return sum(sum_json_no_red(v) for v in node.values())

    return 0


def p2(text: str) -> int:
    return sum_json_no_red(json.loads(text))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
