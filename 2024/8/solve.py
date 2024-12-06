import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos

print(nums("1|2|3|324|2", "|"))

day = 7
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return [row for row in raw_data.strip().split("\n") if row]


def solve_a(raw_data):
    data = prep_data(raw_data)
    ans = 0
    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)
    ans = 0
    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 161, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 48, solve_b(test_data)
# submit(solve_b(lines), part="b", day=day, year=2024)
