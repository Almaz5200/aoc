import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid
from heapq import heappop, heappush, heapify

day = 18
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return [nums(x) for x in raw_data.strip().split("\n")]


def findPath(data, L, lim):
    ans = 0

    corr = set([(a, b) for (a, b) in data[:lim]])

    R, C = L + 1, L + 1

    H = [(0, 0, 0)]
    T = (L, L)

    # for r in range(R):
    #     for c in range(C):
    #         print("." if (c, r) not in corr else "#", end="")
    #     print()
    # print("====")

    s = set()
    while H:
        cost, r, c = heappop(H)

        s.add((r, c))

        if (r, c) in corr:
            continue

        if (r, c) == T:
            return cost

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if valPos(nr, nc, R, C) and (nr, nc) not in s:
                s.add((nr, nc))
                heappush(H, (cost + 1, nr, nc))

    return -1


def solve_a(raw_data, L):
    data = prep_data(raw_data)

    lim = 12 if L == 6 else 1024

    return findPath(data, L, lim)


def solve_b(raw_data, L):
    data = prep_data(raw_data)
    l = 0
    r = len(data)
    ans = 0

    while l <= r:
        m = l + (r - l) // 2
        if findPath(data, L, m + 1) != -1:
            l = m + 1
        else:
            r = m - 1
            ans = m

    return ",".join([str(x) for x in data[ans]])


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data, 6) == 22, solve_a(test_data, 6)
submit(solve_a(lines, 70), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data, 6) == "6,1", solve_b(test_data, 6)
print("ok b")
submit(solve_b(lines, 70), part="b", day=day, year=2024)
