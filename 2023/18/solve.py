import os
import math
import sys
import copy
from typing import Counter, List
from aocd import get_data, submit

day = 18
lines = get_data(day=day, year=2023)

with open("inputr.txt", "w") as f:
    f.write(lines)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    res = []
    for line in ll:
        line = line.split(" ")
        res.append((line[0], int(line[1]), line[2]))

    return res


D = {}


def makeMap(data, x, y):
    if (x, y) in D:
        return

    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return

    if data[x][y] == "#":
        return

    D[(x, y)] = True

    makeMap(data, x + 1, y)
    makeMap(data, x - 1, y)
    makeMap(data, x, y + 1)
    makeMap(data, x, y - 1)


def solve_a(data):
    D.clear()
    map = [["."] * 5000 for _ in [n for n in range(5000)]]
    C = (2500, 2500)
    lx, ly, mx, my = len(map), len(map[0]), 0, 0

    for inst in data:
        d, r, c = inst

        dx, dy = 0, 0
        cx, cy = C
        if d == "R":
            dx = r
        if d == "L":
            dx = -r
        if d == "U":
            dy = -r
        if d == "D":
            dy = r

        C = (cx + dx, cy + dy)

        lx, ly = min(lx, cx), min(ly, cy)
        mx, my = max(mx, cx), max(my, cy)

        fx, tx = cx, cx + dx
        fy, ty = cy, cy + dy

        if fx > tx:
            fx, tx = tx, fx
        if fy > ty:
            fy, ty = ty, fy

        for x in range(fx, tx + 1):
            for y in range(fy, ty + 1):
                map[y][x] = "#"

    nmap = copy.deepcopy(map)

    makeMap(map, 0, 0)
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) not in D:
                nmap[x][y] = "#"
    map = nmap
    # count the number of #
    cnt = sum(
        [1 for x in range(len(map)) for y in range(len(map[0])) if map[x][y] == "#"]
    )

    for x in range(50):
        for y in range(50):
            if map[x][y] == "#":
                print("X", end="")
            else:
                print(".", end="")
        print()

    for x in range(50):
        for y in range(50):
            if (x, y) in D:
                print("X", end="")
            else:
                print(".", end="")
        print()

    return cnt


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 62, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)
