import os
import math
import sys
from functools import cmp_to_key
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re

day = 5
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data
    p1, p2 = raw_data.split("\n\n")
    p1 = [row for row in p1.split("\n") if row]
    p2 = [row for row in p2.split("\n") if row]
    return p1, p2


def solve_a(raw_data):
    r, ordd = prep_data(raw_data)

    PR = defaultdict(list)

    for row in r:
        f, s = row.split("|")
        PR[s].append(f)

    ans = 0
    for ord in ordd:
        seen = set()
        forbs = set()
        g = True
        nums = ord.split(",")
        print(nums, PR)
        for number in nums:

            if number in forbs:
                g = False
                break

            for src in PR[number]:
                if src not in seen:
                    forbs.add(src)

            seen.add(number)

        if g:
            ans += int(nums[len(nums) // 2])

    return ans


def solve_b(raw_data):
    r, ordd = prep_data(raw_data)

    PR = defaultdict(list)

    for row in r:
        f, s = row.split("|")
        PR[s].append(f)

    ans = 0
    incs = []
    for ord in ordd:
        seen = set()
        forbs = set()
        g = True
        nums = ord.split(",")
        print(nums, PR)
        for number in nums:

            if number in forbs:
                g = False
                break

            for src in PR[number]:
                if src not in seen:
                    forbs.add(src)

            seen.add(number)

        if not g:
            incs.append(nums)

    for inc in incs:

        def cmp(a, b):
            if b in PR[a]:
                return 1
            elif a in PR[b]:
                return -1
            else:
                return 0

        inc.sort(key=cmp_to_key(cmp))
        ans += int(inc[len(inc) // 2])

    return ans


with open("test_input.txt", "r") as f:
    test_data = f.read()

assert solve_a(test_data) == 143, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 123, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
