import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict

day = 16
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    return [[c for c in l] for l in ll]


A_C = defaultdict(list)


def trace(x, y, grid, dirc):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return

    if dirc in A_C[(x, y)]:
        return

    A_C[(x, y)].append(dirc)

    dh, dy = dirc

    if grid[x][y] == ".":
        trace(x + dh, y + dy, grid, dirc)

    if grid[x][y] == "/":
        trace(x - dy, y - dh, grid, (-dy, -dh))

    if grid[x][y] == "\\":
        trace(x + dy, y + dh, grid, (dy, dh))

    if grid[x][y] == "|":
        if dh != 0:
            trace(x + dh, y + dy, grid, dirc)
        else:
            trace(x + 1, y, grid, (1, 0))
            trace(x - 1, y, grid, (-1, 0))
    if grid[x][y] == "-":
        if dy != 0:
            trace(x + dh, y + dy, grid, dirc)
        else:
            trace(x, y + 1, grid, (0, 1))
            trace(x, y - 1, grid, (0, -1))


def solve_a(data):
    A_C.clear()
    trace(0, 0, data, (0, 1))

    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in A_C:
                print("#", end="")
            else:
                print(".", end="")
        print()

    return len(A_C)


def solve_b(data):
    n = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (
                not i == 0
                and not j == 0
                and not i == len(data) - 1
                and not j == len(data[0]) - 1
            ):
                continue

            dircs = []
            if i == 0:
                dircs.append((1, 0))
            if j == 0:
                dircs.append((0, 1))
            if i == len(data) - 1:
                dircs.append((-1, 0))
            if j == len(data[0]) - 1:
                dircs.append((0, -1))
            if (i, j) == (0, 3):
                print(dircs)

            for dirc in dircs:
                A_C.clear()
                trace(i, j, data, dirc)

                n = max(len(A_C), n)
    return n


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 46, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 51, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
