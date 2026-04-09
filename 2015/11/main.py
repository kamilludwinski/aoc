# https://adventofcode.com/2015/day/11
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")


def next_password(pwd: str) -> str:
    chars = list(pwd.strip())
    i = len(chars) - 1
    while i >= 0:
        if chars[i] == "z":
            chars[i] = "a"
            i -= 1
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            break

    return "".join(chars)


def has_straight(pwd: str) -> bool:
    for i in range(len(pwd) - 2):
        if ord(pwd[i + 1]) == ord(pwd[i]) + 1 and ord(pwd[i + 2]) == ord(pwd[i]) + 2:
            return True

    return False


def has_two_pairs(pwd: str) -> bool:
    i = 0
    found_one = False

    while i < len(pwd) - 1:
        if pwd[i] == pwd[i + 1]:
            if found_one:
                return True

            found_one = True
            i += 2
        else:
            i += 1

    return False


def is_valid(pwd: str) -> bool:
    if any(c in pwd for c in "iol"):
        return False
    if not has_straight(pwd):
        return False
    if not has_two_pairs(pwd):
        return False

    return True


def next_valid(pwd: str) -> str:
    candidate = next_password(pwd)

    while not is_valid(candidate):
        candidate = next_password(candidate)

    return candidate


def p1(text: str) -> str:
    return next_valid(text)


def p2(text: str) -> str:
    return next_valid(p1(text))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    a1 = p1(text)

    print(a1)
    print(p2(text) if a1 else "")
