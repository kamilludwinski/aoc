# https://adventofcode.com/2015/day/7
import os
from functools import lru_cache

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

U16 = 0xFFFF


def _parse_circuit(text: str) -> dict[str, tuple]:
    circuit: dict[str, tuple] = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        lhs, dest = line.split(" -> ")
        dest = dest.strip()
        parts = lhs.split()

        if len(parts) == 1:
            circuit[dest] = ("PASS", parts[0])
        elif len(parts) == 2 and parts[0] == "NOT":
            circuit[dest] = ("NOT", parts[1])
        elif len(parts) == 3:
            circuit[dest] = (parts[1], parts[0], parts[2])
        else:
            raise ValueError(f"cannot parse: {line!r}")

    return circuit


def evaluate(circuit: dict[str, tuple], target: str = "a") -> int:
    @lru_cache(maxsize=None)
    def signal(name: str) -> int:
        if name.isdigit():
            return int(name) & U16

        op = circuit[name][0]
        if op == "PASS":
            return signal(circuit[name][1])
        if op == "NOT":
            return (~signal(circuit[name][1])) & U16
        if op == "AND":
            _, a, b = circuit[name]
            return signal(a) & signal(b)
        if op == "OR":
            _, a, b = circuit[name]
            return signal(a) | signal(b)
        if op == "LSHIFT":
            _, a, k = circuit[name]
            return (signal(a) << int(k)) & U16
        if op == "RSHIFT":
            _, a, k = circuit[name]
            return signal(a) >> int(k)
        raise ValueError(circuit[name])

    return signal(target)


def run_circuit(text: str, target: str = "a") -> int:
    return evaluate(_parse_circuit(text), target)


def p1(text: str) -> int:
    return run_circuit(text, "a")


def p2(text: str) -> int:
    signal_a = p1(text)
    circuit = _parse_circuit(text)
    circuit["b"] = ("PASS", str(signal_a))
    return evaluate(circuit, "a")


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
