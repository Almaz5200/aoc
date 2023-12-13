import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit

day = 13
lines = get_data(day=day, year=2023)

# sys.setrecursionlimit(100000000)


def parse_input(s):
    s = s.split("\n\n")

    return [s.splitlines() for s in s]


def checkVertical(data, x):
    if x == len(data) - 1:
        return 0

    hm = 0
    broken = False
    for i in range(x + 1, len(data)):
        ind = (x - (i - x)) + 1
        if ind < 0:
            break

        if data[i] != data[ind]:
            broken = True
            break

    if not broken:
        hm = x + 1

    return hm + checkVertical(data, x + 1)


def checkHorizontal(data, y):
    if y == len(data[0]) - 1:
        return 0
    hm = 0
    broken = False
    for i in range(0, len(data)):
        for j in range(y + 1, len(data[0])):
            ind = (y - (j - y)) + 1

            if ind < 0:
                break

            if data[i][j] != data[i][ind]:
                broken = True
                break
        if broken:
            break

    if not broken:
        hm = y + 1

    return hm + checkHorizontal(data, y + 1)


def solve_a(data):
    leftNumbers = 0
    topNumbers = 0

    for d in data:
        left = checkHorizontal(d, 0)
        top = checkVertical(d, 0)

        if left > 0:
            leftNumbers += left
        elif top > 0:
            topNumbers += top

        print("left top", leftNumbers, topNumbers)

    return leftNumbers + topNumbers * 100


def checkVertical_B(data, x):
    if x == len(data) - 1:
        return 0

    hm = 0
    brokens = 0
    for i in range(x + 1, len(data)):
        ind = (x - (i - x)) + 1
        print(i, ind)
        if ind < 0:
            break
        # array of Ture false if equal or not
        comp = [data[i][j] == data[ind][j] for j in range(len(data[0]))]
        falses = comp.count(False)
        brokens += falses

    if brokens == 1:
        hm = x + 1

    return hm + checkVertical_B(data, x + 1)


def checkHorizontal_B(data, y):
    if y == len(data[0]) - 1:
        return 0
    hm = 0
    brokens = 0
    for i in range(0, len(data)):
        for j in range(y + 1, len(data[0])):
            ind = (y - (j - y)) + 1

            if ind < 0:
                break

            if data[i][j] != data[i][ind]:
                brokens += 1

    print(brokens)
    if brokens == 1:
        hm = y + 1

    return hm + checkHorizontal_B(data, y + 1)


def solve_b(data):
    leftNumbers = 0
    topNumbers = 0

    for d in data:
        left = checkHorizontal_B(d, 0)
        top = checkVertical_B(d, 0)

        if left > 0:
            leftNumbers += left
        elif top > 0:
            topNumbers += top

    return leftNumbers + topNumbers * 100


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 405, solve_a(test_data)
print("Solved A")
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 400, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
