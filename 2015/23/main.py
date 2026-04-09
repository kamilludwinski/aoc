# https://adventofcode.com/2015/day/23
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def run(program: list[str], reg_a: int) -> int:
    regs = {"a": reg_a, "b": 0}
    ip = 0
    n = len(program)

    while 0 <= ip < n:
        line = program[ip].strip()
        parts = line.replace(",", "").split()
        op = parts[0]

        if op == "hlf":
            r = parts[1]
            regs[r] //= 2
            ip += 1
        elif op == "tpl":
            r = parts[1]
            regs[r] *= 3
            ip += 1
        elif op == "inc":
            r = parts[1]
            regs[r] += 1
            ip += 1
        elif op == "jmp":
            ip += int(parts[1])
        elif op == "jie":
            r = parts[1]
            if regs[r] % 2 == 0:
                ip += int(parts[2])
            else:
                ip += 1
        elif op == "jio":
            r = parts[1]
            if regs[r] == 1:
                ip += int(parts[2])
            else:
                ip += 1
        else:
            raise ValueError(f"unknown op: {line}")

    return regs["b"]


def p1(text: str) -> int:
    prog = [ln for ln in text.splitlines() if ln.strip()]

    return run(prog, 0)


def p2(text: str) -> int:
    prog = [ln for ln in text.splitlines() if ln.strip()]

    return run(prog, 1)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
