import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit

day = 11
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    return [[c for c in l] for l in ll]


def expand(map):
    new_map = []
    for row in map:
        new_map.append(row.copy())

    for i in range(len(map)):
        ia = len(new_map) - len(map) + i
        if "#" not in map[i]:
            new_map.insert(ia, ["." for _ in range(len(map[i]))])

    for i in range(len(new_map[0])):
        ia = len(new_map[0]) - len(map[0]) + i
        if "#" not in [row[i] for row in map]:
            for j in range(len(new_map)):
                new_map[j].insert(ia, ".")

    return new_map


def solve_a(data):
    m = expand(data)

    gals = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "#":
                gals.append((i, j))

    ans = 0
    for i in range(len(gals)):
        for j in range(len(gals)):
            if i <= j:
                continue

            g1, g2 = gals[i], gals[j]
            dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            ans += dist

    return ans


def solve_b(data):
    m = data

    gals = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "#":
                gals.append((i, j))

    rowsToMult = []
    for i in range(len(m)):
        hasNoGal = True
        for g in gals:
            if g[0] == i:
                hasNoGal = False
                break

        if hasNoGal:
            rowsToMult += [i]

    colsToMult = []
    for i in range(len(m[0])):
        hasNoGal = True
        for g in gals:
            if g[1] == i:
                hasNoGal = False
                break
        if hasNoGal:
            colsToMult += [i]

    for col in reversed(colsToMult):
        for i, g in enumerate(gals):
            if g[1] >= col:
                gals[i] = (g[0], g[1] + 999999)

    for row in reversed(rowsToMult):
        for i, g in enumerate(gals):
            if g[0] >= row:
                gals[i] = (g[0] + 999999, g[1])

    ans = 0
    for i in range(len(gals)):
        for j in range(len(gals)):
            if i <= j:
                continue

            g1, g2 = gals[i], gals[j]
            dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            ans += dist
    return ans


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 374, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

# assert solve_b(test_data) == -1, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
