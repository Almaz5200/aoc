import os
import math
import sys
import functools
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid
from heapq import heappop, heappush

day = 21
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return raw_data.strip().split("\n")
    # return grid(raw_data)


def numPres(path, layer):
    if layer == 1:
        return len(path)

    keypad = [
        [".", "^", "A"],
        ["<", "v", ">"],
    ]
    pos = (0, 2)
    ans = 0

    for ch in path:
        target = fgrid(keypad, ch)
        assert target

        ans += moveCost(pos, target, layer)
        pos = target

    return ans


@functools.lru_cache(maxsize=None)
def moveCost(pos, target, layer):
    ans = math.inf
    Q = deque([(pos, [])])
    while Q:
        place, path = Q.popleft()
        if place == target:
            cost = numPres(path + ["A"], layer - 1)
            ans = min(ans, cost)
            continue

        if place == (0, 0):
            continue

        if place[0] < target[0]:
            Q.append(((place[0] + 1, place[1]), path + ["v"]))
        elif place[0] > target[0]:
            Q.append(((place[0] - 1, place[1]), path + ["^"]))

        if place[1] < target[1]:
            Q.append(((place[0], place[1] + 1), path + [">"]))
        elif place[1] > target[1]:
            Q.append(((place[0], place[1] - 1), path + ["<"]))

    return ans


def moveCostNumeric(pos, target, layers):
    ans = math.inf
    Q = deque([(pos, [])])
    while Q:
        place, path = Q.popleft()
        if place == target:
            cost = numPres(path + ["A"], layers)
            ans = min(ans, cost)
            continue

        if place == (3, 0):
            continue

        if place[0] < target[0]:
            Q.append(((place[0] + 1, place[1]), path + ["v"]))
        elif place[0] > target[0]:
            Q.append(((place[0] - 1, place[1]), path + ["^"]))

        if place[1] < target[1]:
            Q.append(((place[0], place[1] + 1), path + [">"]))
        elif place[1] > target[1]:
            Q.append(((place[0], place[1] - 1), path + ["<"]))

    return ans


def solve(data, layers):
    ans = 0
    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [".", "0", "A"],
    ]

    for code in data:
        val = nums(code)[0]
        len = 0

        pos = fgrid(keypad, "A")
        assert pos
        for ch in code:
            target = fgrid(keypad, ch)
            len += moveCostNumeric(pos, target, layers)
            pos = target

        ans += len * val

    return ans


def solve_a(raw_data):
    data = prep_data(raw_data)
    return solve(data, 3)


def solve_b(raw_data):
    data = prep_data(raw_data)
    return solve(data, 26)


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 126384, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) != 0, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
