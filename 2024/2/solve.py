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
    return [
        [int(x) for x in line.split() if x.strip() != ""]
        for line in raw_data.split("\n")
    ]


def solve_a(raw_data):
    data = prep_data(raw_data)

    safe = 0
    for row in data:
        if not row:
            continue
        fail = False
        seenInc = False
        seenDec = False
        for i, number in enumerate(row[1:]):
            if (abs(number - row[i]) > 3) or (abs(number - row[i]) < 1):
                fail = True
                break

            if row[i] > number:
                seenDec = True
            else:
                seenInc = True

        if fail or (seenInc == seenDec):
            if [fail, seenInc, seenDec] == [False, False, False]:
                assert False
            continue
        safe += 1

    return safe


def isSafe_b(row):
    if not row:
        return False
    fail = False
    seenInc = False
    seenDec = False
    for i, number in enumerate(row[1:]):
        if (abs(number - row[i]) > 3) or (abs(number - row[i]) < 1):
            fail = True
            break

        if row[i] > number:
            seenDec = True
        else:
            seenInc = True

    if fail or (seenInc == seenDec):
        if [fail, seenInc, seenDec] == [False, False, False]:
            assert False
        return False
    return True


def solve_b(raw_data):
    data = prep_data(raw_data)

    safe = 0
    for row in data:
        if isSafe_b(row):
            safe += 1
            continue

        for i in range(len(row)):
            if isSafe_b(row[:i] + row[i + 1 :]):
                safe += 1
                break

    return safe


with open("test_input.txt", "r") as f:
    test_data = f.read()

assert solve_a(test_data) == 2, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 4, solve_b(test_data)
print(solve_b(lines))
submit(solve_b(lines), part="b", day=day, year=2024)
