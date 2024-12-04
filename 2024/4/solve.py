import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re

day = 4
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return [row for row in raw_data.split("\n") if row]


def solve_a(raw_data):
    target = "XMAS"
    data = prep_data(raw_data)

    R, C = len(data), len(data[0])

    def search(r,c,i,dir):
        if i == 4:
            return 1

        if not (0<=r<R and 0<=c<C):
            return 0

        if data[r][c] != target[i]:
            return 0

        return search(r+dir[0],c+dir[1],i+1, dir)


    ans = 0
    for r in range(R):
        for c in range(C):
            dirs = [
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
            ]
            for dir in dirs:
                ans += search(r,c,0,dir)
    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)

    R, C = len(data), len(data[0])

    def search(r,c):
        if not (1<=r<R-1 and 1<=c<C-1):
            return 0

        if data[r][c] != "A":
            return False

        lft = [data[r-1][c-1], data[r+1][c+1]]
        right = [data[r-1][c+1], data[r+1][c-1]]

        if "M" in lft and "M" in right and "S" in lft and "S" in right:
            return 1
        return 0  



    ans = 0
    for r in range(R):
        for c in range(C):
            ans += search(r,c)
    return ans


with open("test_input.txt", "r") as f:
    test_data = f.read()

assert solve_a(test_data) == 18, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

assert solve_b(test_data) == 9, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
