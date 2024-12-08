import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

print(nums("1|2|3|324|2", "|"))

day = 8
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return grid(raw_data)
    # return [row for row in raw_data.strip().split("\n") if row]


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)

    ans = 0
    F = defaultdict(list)
    print(data)
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != ".":
                F[col].append((r, c))

    seen = set()

    for fr in F.keys():
        for i in range(len(F[fr]) - 1):
            for j in range(i + 1, len(F[fr])):
                ar, ac = F[fr][i]
                br, bc = F[fr][j]

                diffr, diffc = br - ar, bc - ac

                p1 = (br + diffr, bc + diffc)
                p2 = (ar - diffr, ac - diffc)

                if valPos(p1[0], p1[1], R, C):
                    ans += 1
                    seen.add(p1)
                if valPos(p2[0], p2[1], R, C):
                    seen.add(p2)

    return len(seen)


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)

    ans = 0
    F = defaultdict(list)
    print(data)
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != ".":
                F[col].append((r, c))

    seen = set()

    for fr in F.keys():
        for i in range(len(F[fr]) - 1):
            for j in range(i + 1, len(F[fr])):
                ar, ac = F[fr][i]
                br, bc = F[fr][j]

                diffr, diffc = br - ar, bc - ac

                p1 = (br + diffr, bc + diffc)

                seen.add((ar, ac))
                seen.add((br, bc))

                while valPos(p1[0], p1[1], R, C):
                    data[p1[0]][p1[1]] = "#"
                    ans += 1
                    seen.add(p1)
                    p1 = (p1[0] + diffr, p1[1] + diffc)

                p2 = (ar - diffr, ac - diffc)
                while valPos(p2[0], p2[1], R, C):
                    data[p2[0]][p2[1]] = "#"
                    seen.add(p2)
                    p2 = (p2[0] - diffr, p2[1] - diffc)
                    print(p2, fr)

    for r in data:
        print(r)
    return len(seen)
    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 14, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 34, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
