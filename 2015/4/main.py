# https://adventofcode.com/2015/day/4
import hashlib
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def p1(secret: str, leading_zeroes: int) -> int:
    prefix = "0" * leading_zeroes
    secret = secret.strip()
    n = 0

    while True:
        n += 1
        digest = hashlib.md5(f"{secret}{n}".encode()).hexdigest()
        if digest.startswith(prefix):
            return n


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        key = f.read()

    print(p1(key, 5))
    print(p1(key, 6))
