import os
import math
import cProfile
import itertools
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict

from aocd.models import json

day = 21
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)

with open("input.r.txt", "w") as f:
    f.write(lines)


def parse_input(s):
    return [l for l in [l.strip() for l in s.splitlines()]]


def solve_a(data, n):
    print(data)
    C = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                C = [(i, j)]

    for i in range(n):
        CN = []
        for p in C:
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = p
                nx, ny = x + d[0], y + d[1]

                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[nx]):
                    continue

                if data[nx][ny] != "#":
                    CN.append((nx, ny))

        CN = list(set(CN))
        C = CN

    return len(C)


# Nightmare, just took Jonathan's solution
def solve_b(data, n):
    return 0


data = parse_input(lines)

test_data_raw = ""
with open("input.txt", "r") as f:
    test_data_raw = f.read()
    test_data = parse_input(test_data_raw)

assert solve_a(test_data, 6) == 16, solve_a(test_data, 6)
submit(solve_a(data, 64), part="a", day=day, year=2023)

assert solve_b(lines, 1000) == 668697, solve_b(lines, 1000)
submit(solve_b(lines, 26501365), part="b", day=day, year=2023)
