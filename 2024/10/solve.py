import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 10
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    g, R, C = grid(raw_data)
    g = [[int(x) for x in r] for r in g]
    return g, R, C


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)
    ans = 0

    heads = []
    for r in range(R):
        for c in range(C):
            if data[r][c] == 0:
                heads.append((r, c))

    for head in heads:
        seenRes = set()
        print(head)

        def find(r, c, h):
            if not valPos(r, c, R, C):
                return 0
            if data[r][c] != h:
                return 0

            if (r, c) in seenRes:
                return 0
            seenRes.add((r, c))

            if h == 9:
                return 1

            resp = 0
            for dr, dc in adj4:
                resp += find(r + dr, c + dc, h + 1)

            return resp

        ans += find(head[0], head[1], 0)

    return ans


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)
    ans = 0

    heads = []
    for r in range(R):
        for c in range(C):
            if data[r][c] == 0:
                heads.append((r, c))

    for head in heads:
        seenRes = set()
        print(head)

        def find(r, c, h):
            if not valPos(r, c, R, C):
                return 0
            if data[r][c] != h:
                return 0

            if h == 9:
                return 1

            resp = 0
            for dr, dc in adj4:
                resp += find(r + dr, c + dc, h + 1)

            return resp

        ans += find(head[0], head[1], 0)

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 36, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 81, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
