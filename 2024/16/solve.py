import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid
from heapq import heappush, heappop

day = 16
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return grid(raw_data)


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)
    ans = 0

    S = fgrid(data, "S")
    E = fgrid(data, "E")

    assert S and E

    H = [(0, S[0], S[1], (0, 1))]

    seen = set()
    while H:
        cost, r, c, dir = heappop(H)
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if data[r][c] == "E":
            return cost

        for dr, dc in adj4:
            ncost = cost + (1 if (dir == (dr, dc) or dir == None) else 1001)
            nr, nc = r + dr, c + dc
            if (nr, nc) in seen or not valPos(nr, nc, R, C) or data[r][c] == "#":
                continue
            heappush(H, (ncost, nr, nc, (dr, dc)))

    return ans


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)
    ans = 0

    S = fgrid(data, "S")
    E = fgrid(data, "E")

    assert S and E

    Ca = {}

    def shortPath(St, E, odir):
        if St == S and E in Ca:
            return Ca[E]
        if St == E:
            return 0, odir
        H = [(0, St[0], St[1], odir)]

        seen = set()
        while H:
            cost, r, c, dir = heappop(H)
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if St == S:
                Ca[(r, c)] = (cost, dir)

            if (r, c) == E:
                return cost, dir

            for dr, dc in adj4:
                ncost = cost + (1 if (dir == (dr, dc) or dir == None) else 1001)
                nr, nc = r + dr, c + dc
                if (nr, nc) in seen or not valPos(nr, nc, R, C) or data[r][c] == "#":
                    continue
                heappush(H, (ncost, nr, nc, (dr, dc)))

        return 0, (0, 0)

    target, _ = shortPath(S, E, (0, 1))
    total = {}

    for r in range(R):
        print(r, R)
        for c in range(C):
            if data[r][c] == "#":
                continue
            a, dr = shortPath(S, (r, c), (0, 1))
            # print(a)
            path = a + shortPath((r, c), E, dr)[0]
            total[(r, c)] = path
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
