import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from aocd.get import re

day = 12
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    return [(c.split()[0], c.split()[1]) for c in ll]


def solve_line_a(line):
    print("==========")
    localArrs = 0
    mp, cn = line
    quos = []

    for i in range(len(mp)):
        if mp[i] == "?":
            quos.append(i)

    # i need to iterate over all 0/1 combinations for each quo
    for i in range(2 ** len(quos)):
        st = [l for l in mp]
        binStr = bin(i)[2:].zfill(len(quos))
        for j in range(len(quos)):
            smbl = "." if binStr[j] == "0" else "#"
            st[quos[j]] = smbl

        rc = "".join(st).split(".")
        rc = [len(c) for c in rc if c != ""]
        if rc == [int(c) for c in cn.split(",")]:
            print("".join(st))
            localArrs += 1
    return localArrs


def solve_a(data):
    arrs = 0
    for line in data:
        arrs += solve_line_a(line)

    return arrs


# This p2 totaly came from Jonathan Paulson
DP = {}


def rec(mp, blocks, i, bi, current):
    key = (i, bi, current)
    if key in DP:
        return DP[key]
    if i == len(mp):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and current == blocks[bi]:
            return 1
        else:
            return 0

    ans = 0
    for c in [".", "#"]:
        if mp[i] == c or mp[i] == "?":
            if c == "." and current == 0:
                ans += rec(mp, blocks, i + 1, bi, 0)
            elif (
                c == "." and current > 0 and bi < len(blocks) and current == blocks[bi]
            ):
                ans += rec(mp, blocks, i + 1, bi + 1, 0)
            elif c == "#":
                ans += rec(mp, blocks, i + 1, bi, current + 1)
    DP[key] = ans
    return ans


def solve_b(data):
    arrs = 0
    for line in data:
        DP.clear()
        mp, cn = line

        mp = "?".join([mp, mp, mp, mp, mp])
        cn = ",".join([cn, cn, cn, cn, cn])

        cn = [int(c) for c in cn.split(",")]

        arrs += rec(mp, cn, 0, 0, 0)

    return arrs


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 21, solve_a(test_data)
# submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 525152, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
