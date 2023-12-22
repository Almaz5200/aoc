import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 22
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ms = []
    for line in s.splitlines():
        k = line.split(" -> ")
        ds = k[1].split(", ")
        mt, mn = "", ""
        if k[0] == "broadcaster":
            mt = "b"
            mn = "broadcaster"
        else:
            mt = k[0][0]
            mn = k[0][1:]

        ms.append((mt, mn, ds))

    return ms


def solve_a(data):
    return lows * highs


def solve_b(data):
    return 0


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 11687500, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

submit(solve_b(data), part="b", day=day, year=2023)
