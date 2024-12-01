import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter

from aocd.models import json

day = 1
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def solve_a(data):
    a = []
    b = []
    for line in data.split("\n"):
        if not line:
            continue
        na, nb = line.split()
        a.append(int(na))
        b.append(int(nb))

    a.sort()
    b.sort()
    ans = 0

    for i in range(len(a)):
        ans += abs(a[i] - b[i])

    return ans


def solve_b(data):
    a = []
    b = []
    for line in data.split("\n"):
        if not line:
            continue
        na, nb = line.split()
        a.append(int(na))
        b.append(int(nb))

    bc = Counter(b)
    ans = 0

    for i in range(len(a)):
        ans += a[i] * bc[a[i]]

    return ans


with open("test_input.txt", "r") as f:
    test_data = f.read()

assert solve_a(test_data) == 11, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 31, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
