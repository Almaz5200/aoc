import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 23
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    lns = s.splitlines()
    lns = [[l for l in ln] for ln in lns]
    return lns


def options(data, pos, can_climb):
    x, y = pos
    opts = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

    if not can_climb:
        sym = data[y][x]
        if sym == ">":
            return [(x + 1, y)]
        if sym == "<":
            return [(x - 1, y)]
        if sym == "^":
            return [(x, y - 1)]
        if sym == "v":
            return [(x, y + 1)]

    opts = [(x, y) for x, y in opts if 0 <= x < len(data[0]) and 0 <= y < len(data)]
    opts = [(x, y) for x, y in opts if data[y][x] != "#"]

    return opts


def walk(data, pos, seen, target, can_climb):
    if pos == target:
        return 1

    nseen = seen.copy()

    nseen.add(pos)
    opts = options(data, pos, can_climb)
    opts = [opt for opt in opts if opt not in seen]

    if len(opts) == 0:
        return -1

    return 1 + max(walk(data, opt, nseen, target, can_climb) for opt in opts)


def solve_a(data):
    print(data)

    start = (0, data[0].index("."))
    end = (len(data[0]) - 1, data[-1].index("."))

    return walk(data, start, set(), end, False) + 1


def solve_b(data):
    sy, sx = (0, data[0].index("."))
    ey, ex = (len(data[0]) - 1, data[-1].index("."))

    Q = deque([(sy, sx, 0, set())])
    res = 0
    while Q:
        y, x, d, seen = Q.pop()
        if (y, x) == (ey, ex):
            res = max(d, res)
            print(res)

        nseen = seen.copy()
        nseen.add((y, x))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not (0 <= y + dy < len(data) and 0 <= x + dx < len(data[0])):
                continue
            if (y + dy, x + dx) in seen:
                continue
            if data[y + dy][x + dx] == "#":
                continue

            Q.append((y + dy, x + dx, d + 1, nseen))

    return res


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 94, solve_a(test_data)
# submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 154, solve_b(test_data)
print("huh")
submit(solve_b(data), part="b", day=day, year=2023)
