# https://adventofcode.com/2015/day/21
import os
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

if not os.path.exists("input.txt"):
    raise FileNotFoundError("input.txt not found")

PLAYER_HP = 100


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


WEAPONS = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

ARMOR = [
    Item("None", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

RINGS = [
    Item("None0", 0, 0, 0),
    Item("None1", 0, 0, 0),
    Item("Damage+1", 25, 1, 0),
    Item("Damage+2", 50, 2, 0),
    Item("Damage+3", 100, 3, 0),
    Item("Defense+1", 20, 0, 1),
    Item("Defense+2", 40, 0, 2),
    Item("Defense+3", 80, 0, 3),
]


def parse_boss(text: str) -> tuple[int, int, int]:
    hp = dmg = arm = 0
    for line in text.strip().splitlines():
        line = line.strip()
        if line.startswith("Hit Points:"):
            hp = int(line.split()[-1])
        elif line.startswith("Damage:"):
            dmg = int(line.split()[-1])
        elif line.startswith("Armor:"):
            arm = int(line.split()[-1])

    return hp, dmg, arm


def player_wins(
    player_dmg: int, player_armor: int, boss_hp: int, boss_dmg: int, boss_armor: int
) -> bool:
    p_hp = PLAYER_HP
    b_hp = boss_hp
    while True:
        b_hp -= max(1, player_dmg - boss_armor)
        if b_hp <= 0:
            return True

        p_hp -= max(1, boss_dmg - player_armor)
        if p_hp <= 0:
            return False


def ring_pairs() -> Iterable[tuple[Item, Item]]:
    ring_items = RINGS[2:]
    yield (RINGS[0], RINGS[1])
    for r in ring_items:
        yield (RINGS[0], r)
        yield (r, RINGS[0])
    for a, b in combinations(ring_items, 2):
        yield (a, b)


def loadouts() -> Iterable[tuple[int, int, int]]:
    for w in WEAPONS:
        for a in ARMOR:
            for r1, r2 in ring_pairs():
                cost = w.cost + a.cost + r1.cost + r2.cost
                dmg = w.damage + a.damage + r1.damage + r2.damage
                arm = w.armor + a.armor + r1.armor + r2.armor

                yield cost, dmg, arm


def p1(text: str) -> int:
    boss_hp, boss_dmg, boss_armor = parse_boss(text)
    best = 10**9

    for cost, dmg, arm in loadouts():
        if player_wins(dmg, arm, boss_hp, boss_dmg, boss_armor):
            best = min(best, cost)

    return best


def p2(text: str) -> int:
    boss_hp, boss_dmg, boss_armor = parse_boss(text)
    worst = 0

    for cost, dmg, arm in loadouts():
        if not player_wins(dmg, arm, boss_hp, boss_dmg, boss_armor):
            worst = max(worst, cost)

    return worst


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    print(p1(text))
    print(p2(text))
