import os
import math
import numpy as np
import sys
import copy
import sympy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 24
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    lin = s.splitlines()
    l = [l.split(" @ ") for l in lin]
    r = [(p[0].split(", "), p[1].split(", ")) for p in l]
    res = []
    for k in r:
        res.append(
            (
                (int(k[0][0]), int(k[0][1]), int(k[0][2])),
                (int(k[1][0]), int(k[1][1]), int(k[1][2])),
            )
        )

    return res


def intersect(ax, ay, avx, avy, bx, by, bvx, bvy):
    if avx / avy == bvx / bvy:
        dx = bx - ax
        dy = by - ay

        return None

    b1, b2 = 1, 1
    a1, a2 = avy / avx, bvy / bvx

    c1 = -a1 * ax + b1 * ay
    c2 = -a2 * bx + b2 * by

    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
    y = -y

    if ((x < ax) != (avx < 0)) or ((x < bx) != (bvx < 0)):
        return None

    if ((y < ay) != (avy < 0)) or ((y < by) != (bvy < 0)):
        return None

    return x, y


def solve_a(data, st, en):
    print(data)
    ints = 0
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            if i == j:
                continue
            (ax, ay, _), (avx, avy, _) = data[i]
            (bx, by, _), (bvx, bvy, _) = data[j]

            pt = intersect(ax, ay, avx, avy, bx, by, bvx, bvy)
            if pt is None:
                continue

            iX, iY = pt
            print(pt)

            if st <= iX <= en and st <= iY <= en:
                ints += 1

    return ints


# reddit user u/hugues_hoppe
def day24_part2(s):
    array = np.array(
        [line.replace("@", ",").split(",") for line in s.splitlines()], int
    )
    p, v, t = (sympy.symbols(f"{ch}(:3)") for ch in "pvt")
    equations = [
        array[i, j] + t[i] * array[i, 3 + j] - p[j] - v[j] * t[i]
        for i in range(3)
        for j in range(3)
    ]
    return sum(sympy.solve(equations, (*p, *v, *t))[0][:3])


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data_raw = f.read()
    test_data = parse_input(test_data_raw)

assert solve_a(test_data, 7, 27) == 2, solve_a(test_data, 7, 27)
# submit(solve_a(data, 200000000000000, 400000000000000), part="a", day=day, year=2023)

assert day24_part2(test_data_raw) == 47, day24_part2(test_data_raw)
submit(day24_part2(lines), part="b", day=day, year=2023)
