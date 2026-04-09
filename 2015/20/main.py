# https://adventofcode.com/2015/day/20
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def target_presents(text: str) -> int:
    return int(text.strip())


def min_house_sieve(target: int, *, part2: bool) -> int:
    limit = max(500_000, target // 8 + 10_000)

    while True:
        presents = [0] * limit
        if not part2:
            for elf in range(1, limit):
                step = 10 * elf
                for h in range(elf, limit, elf):
                    presents[h] += step
        else:
            for elf in range(1, limit):
                step = 11 * elf
                for m in range(1, 51):
                    h = elf * m
                    if h < limit:
                        presents[h] += step
        for h in range(1, limit):
            if presents[h] >= target:
                return h

        limit *= 2


def p1(text: str) -> int:
    return min_house_sieve(target_presents(text), part2=False)


def p2(text: str) -> int:
    return min_house_sieve(target_presents(text), part2=True)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
