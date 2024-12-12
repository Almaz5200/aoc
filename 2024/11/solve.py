import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 11
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return nums(raw_data.strip())


def solve_all(data, num):
    for i in range(num):
        print(i, len(data))
        nxt = defaultdict(int)
        for number in data.keys():
            lg = int(math.log(number, 10)) if number != 0 else 0
            if number == 0:
                nxt[1] += data[number]
            elif lg % 2 == 1:
                lg //= 2
                lg += 1
                nxt[number // (10**lg)] += data[number]
                nxt[number % (10**lg)] += data[number]
            else:
                nxt[number * 2024] += data[number]

        data = nxt

    return sum(data.values())


def solve_a(raw_data):
    data = Counter(prep_data(raw_data))
    return solve_all(data, 25)

    # ans = 0
    # return ans


def solve_b(raw_data):
    data = Counter(prep_data(raw_data))
    return solve_all(data, 75)


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 55312, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

# if test_data:
#     assert solve_b(test_data) == 48, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
