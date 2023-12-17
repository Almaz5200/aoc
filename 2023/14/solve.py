from collections import defaultdict
import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from aocd.models import time

day = 14
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    return [[c for c in l] for l in ll]


def solve_a(data):
    load = 0
    for j in range(len(data[0])):
        nextLoad = len(data)
        for i in range(len(data)):
            if data[i][j] == "O":
                load += nextLoad
                nextLoad -= 1
            if data[i][j] == "#":
                nextLoad = len(data) - i - 1

    return load


def calcLoad(data):
    load = 0
    for j in range(len(data[0])):
        for i in range(len(data)):
            if data[i][j] == "O":
                load += len(data) - i

    return load


loads = defaultdict(list)


def solve_b(data):
    dat = data

    for k in range(230):
        print(k)

        for _ in range(4):
            for j in range(len(dat[0])):
                nextPos = 0
                for i in range(len(dat)):
                    if dat[i][j] == "O":
                        dat[i][j] = "."
                        dat[nextPos][j] = "O"
                        nextPos += 1
                    if dat[i][j] == "#":
                        nextPos = i + 1

            dat = list(zip(*dat[::-1]))
            dat = [list(l) for l in dat]

        loads[calcLoad(dat)].append(k)

        if len(loads[calcLoad(dat)]) > 0:
            print(k, calcLoad(dat), loads[calcLoad(dat)])

    return calcLoad(dat)


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 136, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 64, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
