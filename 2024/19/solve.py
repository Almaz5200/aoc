import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 19
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    av, de = raw_data.strip().split("\n\n")
    av = av.split(", ")
    de = de.split("\n")

    return av, de

    # return grid(raw_data)


def solve_a(raw_data):
    av, des = prep_data(raw_data)
    ans = 0

    def canBuild(tow):
        if tow == "":
            return True

        for d in av:
            if tow[: len(d)] == d:
                if canBuild(tow[len(d) :]):
                    return True

        return False

    ans = 0

    for d in des:
        if canBuild(d):
            ans += 1

    return ans


def solve_b(raw_data):
    av, des = prep_data(raw_data)
    ans = 0

    C = {}

    def canBuild(tow):
        if tow in C:
            return C[tow]
        if tow == "":
            return 1

        ans = 0
        for d in av:
            if tow[: len(d)] == d:
                ans += canBuild(tow[len(d) :])

        C[tow] = ans
        return ans

    ans = 0

    for d in des:
        ans += canBuild(d)

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 6, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 16, solve_b(test_data)
print("test ok")
submit(solve_b(lines), part="b", day=day, year=2024)
