# https://adventofcode.com/2019/day/2
import os

def run_intcode(prog):
    prog = prog[:]
    ip = 0
    while True:
        op = prog[ip]
        if op == 1:
            prog[prog[ip+3]] = prog[prog[ip+1]] + prog[prog[ip+2]]
        elif op == 2:
            prog[prog[ip+3]] = prog[prog[ip+1]] * prog[prog[ip+2]]
        elif op == 99:
            break
        else:
            raise Exception(f"Unknown opcode {op}")
        ip += 4
    return prog

def p1(text: str) -> int:
    prog = list(map(int, text.strip().split(',')))
    prog[1], prog[2] = 12, 2
    return run_intcode(prog)[0]

def p2(text: str) -> int:
    orig = list(map(int, text.strip().split(',')))
    for noun in range(100):
        for verb in range(100):
            prog = orig[:]
            prog[1], prog[2] = noun, verb
            try:
                if run_intcode(prog)[0] == 19690720:
                    return 100 * noun + verb
            except Exception:
                continue
    return -1

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path, "r") as file:
        text = file.read().strip()
    print(p1(text))
    print(p2(text))
