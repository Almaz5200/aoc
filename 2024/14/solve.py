import os
import time
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 14
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    data = []
    for line in raw_data.strip().split("\n"):
        p, v = line.split(" ")
        _, p = p.split("=")
        _, v = v.split("=")
        print(line)
        p = nums(p)
        v = nums(v)
        data.append((p, v))
    return data


def solve_a(raw_data, R, C):
    data = prep_data(raw_data)
    print(data)
    ans = 0

    qs = [0, 0, 0, 0]

    for rob in data:
        a, b = rob
        r, c = a
        dr, dc = b

        print(r, c)
        r += 100 * dr
        c += 100 * dc

        r %= R
        c %= C
        print(r, c)

        if r == R // 2 or c == C // 2:
            print("skip")
            print("==")
            continue
        print("==")

        CC = 0
        if r > (R // 2):
            CC += 1
        if c > (C // 2):
            CC += 2
        qs[CC] += 1

    for l in qs:
        print(l)
    ans = 1
    for q in qs:
        ans *= q
    return ans


def solve_b(raw_data):
    R, C = 101, 103
    data = prep_data(raw_data)
    print(data)
    ans = 0

    qs = [0, 0, 0, 0]
    pos = {}
    for i, rob in enumerate(data):
        a, b = rob
        r, c = a

        pos[i] = (r, c)

    iter = 0
    while True:
        N = defaultdict(int)
        for i, rob in enumerate(data):
            a, b = rob
            r, c = pos[i]
            dr, dc = b

            r += 1 * dr
            c += 1 * dc

            r %= R
            c %= C

            pos[i] = (r, c)
            N[(r, c)] += 1

            if r == R // 2 or c == C // 2:
                continue

            CC = 0
            if r > (R // 2):
                CC += 1
            if c > (C // 2):
                CC += 2
            qs[CC] += 1

        iter += 1
        print(iter)
        for r in range(R):
            for c in range(C):
                print(N[(r, c)], end="")

            print()

    for l in qs:
        print(l)
    ans = 1
    for q in qs:
        ans *= q
    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data, 11, 7) == 12, solve_a(test_data, 11, 7)
p1 = solve_a(lines, 101, 103)
assert p1 != 0
submit(p1, part="a", day=day, year=2024)

# if test_data:
#     assert solve_b(test_data) != 0, solve_b(test_data)
p2 = solve_b(lines)
assert p2 != 0
submit(p2, part="b", day=day, year=2024)
