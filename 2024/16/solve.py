import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, fgrid, Grid
from heapq import heappush, heappop

day = 16
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    data = Grid(raw_data)
    data.walls = ["#"]
    return data


def solve_a(raw_data):
    data = prep_data(raw_data)
    ans = 0

    S = data.find("S")
    E = data.find("E")

    assert S and E

    H = [(0, S, (0, 1))]

    seen = set()
    while H:
        cost, pos, dir = heappop(H)
        if pos in seen:
            continue
        seen.add(pos)

        if data[pos] == "E":
            return cost

        for ndir, npos, _ in data.dirAdj4(pos):
            ncost = cost + (1 if (dir == ndir or dir is None) else 1001)
            if npos in seen:
                continue
            heappush(H, (ncost, npos, ndir))

    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)
    ans = 0

    S = data.find("S")
    E = data.find("E")

    assert S and E

    Ca = {}

    def shortPath(St, E, odir):
        if St == S and E in Ca:
            return Ca[E]
        if St == E:
            return 0, odir
        H = [(0, St, odir)]

        seen = set()
        while H:
            cost, pos, dir = heappop(H)
            if pos in seen:
                continue
            seen.add(pos)

            if St == S:
                Ca[pos] = (cost, dir)

            if pos == E:
                return cost, dir

            for ndir, npos, _ in data.dirAdj4(pos):
                ncost = cost + (1 if (dir == ndir or dir == None) else 1001)
                if npos in seen:
                    continue
                heappush(H, (ncost, npos, ndir))

        return 0, (0, 0)

    target, _ = shortPath(S, E, (0, 1))
    total = {}

    for pos, val in data:
        if val == "#":
            continue
        a, dr = shortPath(S, pos, (0, 1))
        # print(a)
        path = a + shortPath(pos, E, dr)[0]
        total[pos] = path
        if path <= target:
            assert path == target
            ans += 1

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 11048, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 64, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
