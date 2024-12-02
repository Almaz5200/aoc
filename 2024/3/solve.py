import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter

from aocd.models import json

day = 2
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return raw_data.split("\n")


def solve_a(raw_data):
    data = prep_data(raw_data)
    return 0


def solve_b(raw_data):
    data = prep_data(raw_data)
    return 0


with open("test_input.txt", "r") as f:
    test_data = f.read()

# assert solve_a(test_data) == 11, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 31, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
