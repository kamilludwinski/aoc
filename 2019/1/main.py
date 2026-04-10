# https://adventofcode.com/2019/day/1
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
if not os.path.exists(input_path):
    raise FileNotFoundError("input.txt not found")


def p1(text: str) -> int:
    return sum(int(line) // 3 - 2 for line in text.splitlines() if line.strip())


def p2(text: str) -> int:
    def fuel(mass: int) -> int:
        total = 0
        while True:
            mass = mass // 3 - 2
            if mass <= 0:
                break
            total += mass
        return total

    return sum(fuel(int(line)) for line in text.splitlines() if line.strip())


if __name__ == "__main__":
    with open(input_path, "r") as file:
        text = file.read().strip()
    print(p1(text))
    print(p2(text))
