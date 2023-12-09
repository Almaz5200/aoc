import os
import math
import sys
from typing import List
from aocd import get_data, submit

day = 9
lines = get_data(day=day, year=2023)


def parse_input(s):
    lines = s.splitlines()
    numbers = [line.split() for line in lines]
    cn = [[int(no) for no in n] for n in numbers]

    return cn


def get_next(seq):
    if all([x == 0 for x in seq]):
        return 0
    ns = []
    for i in range(len(seq) - 1):
        ns.append(seq[i + 1] - seq[i])

    return seq[-1] + get_next(ns)


def solve_a(data):
    result = 0
    for s in data:
        result += get_next(s)

    return result


def get_prev(seq):
    if all([x == 0 for x in seq]):
        return 0
    ns = []
    for i in range(len(seq) - 1):
        ns.append(seq[i + 1] - seq[i])

    return seq[0] - get_prev(ns)


def solve_b(data):
    result = 0
    for s in data:
        result += get_prev(s)

    return result


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 114
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 2, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
