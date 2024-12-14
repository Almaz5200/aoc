import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 13
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    lines = raw_data.strip().split("\n")
    data = []
    for i in range(0, len(lines), 4):
        a, b, c = lines[i], lines[i + 1], lines[i + 2]
        p = r".*: X[+=](\d+), Y[+=](\d+)"
        # print(a)
        ma = re.match(p, a)
        mb = re.match(p, b)
        mc = re.match(p, c)
        # print(mat.group(1))
        # print(mat.group(2))
        if ma and mb and mc:
            data.append(
                [
                    [int(ma.group(1)), int(ma.group(2))],
                    [int(mb.group(1)), int(mb.group(2))],
                    [int(mc.group(1)), int(mc.group(2))],
                ]
            )

    return data


def solve_a(raw_data):
    data = prep_data(raw_data)
    res = 0

    def vlen(a, b):
        return math.sqrt(a**2 + b**2)

    def search(a, b, target, depth):
        if depth > 100:
            return float("inf")

        if target[0] == 0 and target[1] == 0:
            return 0

        if target[0] < 0 or target[1] < 0:
            return float("inf")
        print(target, depth)

        ans = search(a, b, (target[0] - a[0], target[1] - a[1]), depth + 1) + 3
        ans = min(
            ans, search(a, b, (target[0] - b[0], target[1] - b[1]), depth + 1) + 1
        )

        return ans

    for a, b, t in data:
        ans = float("inf")

        for aas in range(101):
            for bs in range(101):
                if aas == 80 and bs == 40:
                    # print(bs)
                    print(
                        t[0], (aas * a[0] + bs * b[0]), t[1], (aas * a[1] + bs * b[1])
                    )
                if t[0] == (aas * a[0] + bs * b[0]) and t[1] == (
                    aas * a[1] + bs * b[1]
                ):
                    print("hit!")
                    ans = min(ans, aas * 3 + bs)

        if ans < float("inf"):
            print(res, ans)
            res += ans

    return res


def solve_b(raw_data):
    data = prep_data(raw_data)
    res = 0

    def search(a, b, target, depth):
        if depth > 100:
            return float("inf")

        if target[0] == 0 and target[1] == 0:
            return 0

        if target[0] < 0 or target[1] < 0:
            return float("inf")
        print(target, depth)

        ans = search(a, b, (target[0] - a[0], target[1] - a[1]), depth + 1) + 3
        ans = min(
            ans, search(a, b, (target[0] - b[0], target[1] - b[1]), depth + 1) + 1
        )

        return ans

    for a, b, t in data:
        ## Got this idea from reddit, didn't come up myself, unfortunately :(
        tx, ty = (t[0] + 10000000000000, t[1] + 10000000000000)
        ax, ay = a
        bx, by = b

        b = (tx * ay - ty * ax) // (ay * bx - by * ax)
        a = (tx * by - ty * bx) // (by * ax - bx * ay)

        if ax * a + bx * b == tx and ay * a + by * b == ty:
            res += a * 3 + b

    return res


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 480, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) != 0, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
