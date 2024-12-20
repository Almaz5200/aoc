import os
import math
import sys
import copy
from typing import List

from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 6
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return grid(raw_data)


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)

    guard_pos = fgrid(data, "^")
    if not guard_pos:
        return -1

    sdir = set()
    splace = set()

    dirs = adj4
    dir = 0

    while 0 <= guard_pos[0] < R and 0 <= guard_pos[1] < C:
        if (guard_pos, dir) in sdir:
            break
        sdir.add((guard_pos, dir))
        splace.add(guard_pos)

        pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        while 0 <= pot[0] < R and 0 <= pot[1] < C and data[pot[0]][pot[1]] == "#":
            dir += 1
            pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        guard_pos = pot

    return len(splace)


def haveLoop(data, guard_pos):
    R, C = len(data), len(data[0])

    sdir = set()
    splace = set()

    dirs = adj4
    dir = 0

    loop = False
    while 0 <= guard_pos[0] < R and 0 <= guard_pos[1] < C:
        if (guard_pos, dir % 4) in sdir:
            loop = True
            break
        sdir.add((guard_pos, dir % 4))
        splace.add(guard_pos)

        pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        while 0 <= pot[0] < R and 0 <= pot[1] < C and data[pot[0]][pot[1]] == "#":
            dir += 1
            pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        guard_pos = pot

    return loop


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)
    ans = 0

    ini_guard_pos = fgrid(data, "^")

    guard_pos = ini_guard_pos
    assert guard_pos is not None

    sdir = set()
    splace = set()

    dirs = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    dir = 0

    while 0 <= guard_pos[0] < R and 0 <= guard_pos[1] < C:
        if (guard_pos, dir) in sdir:
            break
        sdir.add((guard_pos, dir))
        splace.add(guard_pos)

        pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        while 0 <= pot[0] < R and 0 <= pot[1] < C and data[pot[0]][pot[1]] == "#":
            dir += 1
            pot = (guard_pos[0] + dirs[dir % 4][0], guard_pos[1] + dirs[dir % 4][1])

        guard_pos = pot

    print("stargin", len(data))
    for r in range(R):
        print(r)
        for c in range(C):
            if data[r][c] == "." and (r, c) in splace:
                data[r][c] = "#"
                if haveLoop(data, ini_guard_pos):
                    ans += 1
                data[r][c] = "."
    return ans


with open("2024/6/test_input.txt", "r") as f:
    test_data = f.read().strip()

if len(test_data) > 0:
    assert solve_a(test_data) == 41, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 6, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
