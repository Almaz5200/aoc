import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re

day = 3
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return raw_data


def solve_a(raw_data):
    data = prep_data(raw_data)

    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    ans = 0
    for match in re.findall(pattern, data):
        print(match)
        ans += int(match[0]) * int(match[1])


    print(ans)
    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)

    pattern = r"do\(\)|don't\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    regex = re.compile(pattern)
    ans = 0
    isActive = True
    for match in regex.finditer(data):
        if match.group(0) == "do()":
            isActive=True
        elif match.group(0) == "don't()": 
            isActive = False
        elif isActive:
            ans += int(match.group(1)) * int(match.group(2))


    print(ans)
    return ans


with open("test_input.txt", "r") as f:
    test_data = f.read()

assert solve_a(test_data) == 161, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 48, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
