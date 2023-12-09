import os
import math
import sys
from typing import List
from aocd import get_data, submit

day = 8
lines = get_data(day=day, year=2023)


def parse_input(s):
    lines = s.splitlines()
    return lines


def solve_a(data):
    return 0


def solve_b(data):
    return 0


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == -1
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_a(test_data) == -1
submit(solve_b(data), part="b", day=day, year=2023)
