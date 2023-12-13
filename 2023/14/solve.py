import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit

day = 12
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    return [[c for c in l] for l in ll]


def solve_a(data):
    return 0


def solve_b(data):
    return 0


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 374, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == -1, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
