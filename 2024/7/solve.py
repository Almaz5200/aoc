import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 7
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return raw_data.strip().split("\n")
    # return grid(raw_data)


def solve_a(raw_data):
    data = prep_data(raw_data)
    ans = 0
    for l in data:
        t, nm = l.split(": ")
        nms = nums(nm)
        t = int(t)

        def search(cur, i):
            if i == len(nms):
                return cur == t

            if cur > t:
                return False

            if search(cur + nms[i], i + 1):
                return True
            if search(cur * nms[i], i + 1):
                return True

            return False

        if search(0, 0):
            ans += t

    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)
    ans = 0
    for l in data:
        t, nm = l.split(": ")
        nms = nums(nm)
        t = int(t)

        def search(cur, i):
            if i == len(nms):
                return cur == t

            if cur > t:
                return False

            if search(cur + nms[i], i + 1):
                return True
            if search(cur * nms[i], i + 1):
                return True
            if search(int(str(cur) + str(nms[i])), i + 1):
                return True

            return False

        if search(0, 0):
            ans += t

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 3749, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 11387, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
