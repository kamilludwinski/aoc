# https://adventofcode.com/2015/day/22
import heapq
import os

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

PLAYER_HP_START = 50
PLAYER_MANA_START = 500


def parse_boss(text: str) -> tuple[int, int]:
    hp = dmg = 0
    for line in text.strip().splitlines():
        line = line.strip()
        if line.startswith("Hit Points:"):
            hp = int(line.split()[-1])
        elif line.startswith("Damage:"):
            dmg = int(line.split()[-1])
    return hp, dmg


def apply_start_of_turn(
    hp: int,
    mana: int,
    boss_hp: int,
    shield: int,
    poison: int,
    recharge: int,
) -> tuple[int, int, int, int, int, int, int]:
    armor = 7 if shield > 0 else 0
    if poison > 0:
        boss_hp -= 3
        poison -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1
    if shield > 0:
        shield -= 1
    return hp, mana, boss_hp, shield, poison, recharge, armor


def min_mana_to_win(boss_hp: int, boss_dmg: int, *, hard: bool) -> int:
    pq: list[tuple[int, int, int, int, int, int, int, bool]] = []
    heapq.heappush(
        pq,
        (0, PLAYER_HP_START, PLAYER_MANA_START, boss_hp, 0, 0, 0, True),
    )
    seen: set[tuple[int, int, int, int, int, int, bool]] = set()

    while pq:
        spent, hp, mana, bhp, sh, po, rc, turn = heapq.heappop(pq)
        key = (hp, mana, bhp, sh, po, rc, turn)
        if key in seen:
            continue
        seen.add(key)

        hp, mana, bhp, sh, po, rc, armor = apply_start_of_turn(
            hp, mana, bhp, sh, po, rc
        )
        if bhp <= 0:
            return spent

        if turn:
            if hard:
                hp -= 1
            if hp <= 0:
                continue

            if mana >= 53:
                nb = bhp - 4
                if nb <= 0:
                    return spent + 53
                heapq.heappush(
                    pq,
                    (spent + 53, hp, mana - 53, nb, sh, po, rc, False),
                )
            if mana >= 73:
                nb = bhp - 2
                nh = hp + 2
                if nb <= 0:
                    return spent + 73
                heapq.heappush(
                    pq,
                    (spent + 73, nh, mana - 73, nb, sh, po, rc, False),
                )
            if mana >= 113 and sh == 0:
                heapq.heappush(
                    pq,
                    (spent + 113, hp, mana - 113, bhp, 6, po, rc, False),
                )
            if mana >= 173 and po == 0:
                heapq.heappush(
                    pq,
                    (spent + 173, hp, mana - 173, bhp, sh, 6, rc, False),
                )
            if mana >= 229 and rc == 0:
                heapq.heappush(
                    pq,
                    (spent + 229, hp, mana - 229, bhp, sh, po, 5, False),
                )
        else:
            dmg = max(1, boss_dmg - armor)
            hp -= dmg
            if hp <= 0:
                continue
            heapq.heappush(pq, (spent, hp, mana, bhp, sh, po, rc, True))

    raise RuntimeError("no winning sequence")


def p1(text: str) -> int:
    bhp, bd = parse_boss(text)
    return min_mana_to_win(bhp, bd, hard=False)


def p2(text: str) -> int:
    bhp, bd = parse_boss(text)
    return min_mana_to_win(bhp, bd, hard=True)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
