import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

print(nums("1|2|3|324|2", "|"))

day = 9
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    return [int(x) for x in raw_data.strip()]
    # return [row for row in raw_data.strip().split("\n") if row]


def solve_a(raw_data):
    data = prep_data(raw_data)

    files = []
    spaces = []

    for i in range(0, len(data), 2):
        files.append(data[i])
        if len(data) > i + 1:
            spaces.append(data[i + 1])

    spaces = spaces[::-1]

    pos = 0
    ans = 0
    filesi = 0
    while files or spaces:
        if filesi < len(files):
            nm = files[filesi]
            for _ in range(nm):
                ans += filesi * pos
                print(f"{filesi} * {pos}")
                pos += 1

            filesi += 1
        else:
            break

        if spaces:
            space = spaces.pop()
            while space and filesi < len(files):
                files[-1] -= 1
                ans += (len(files) - 1) * pos
                pos += 1
                print(f"{len(files)-1} * {pos}")
                if files[-1] == 0:
                    files.pop()

                space -= 1

    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)

    files = []
    spaces = []

    for i in range(0, len(data), 2):
        files.append(data[i])
        if len(data) > i + 1:
            spaces.append(data[i + 1])

    # spaces = spaces[::-1]

    idnum_per_space = defaultdict(list)

    for i, file in reversed(list(enumerate(files))):
        for j, space in enumerate(spaces):
            if space >= file and i > j:
                idnum_per_space[j].append((i, file))

                spaces[j] -= file
                spaces[i - 1] += file
                break

    seen = set()
    pos = 0
    ans = 0
    for i, file in enumerate(files):
        if i not in seen:
            for _ in range(file):
                ans += i * pos
                seen.add(i)
                print("a", i, pos)
                pos += 1

        print(idnum_per_space[i])
        for k, file in idnum_per_space[i]:
            for _ in range(file):
                print("b", k, pos)
                seen.add(k)
                ans += k * pos
                pos += 1

        if i < len(spaces):
            pos = pos + spaces[i]

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

# if test_data:
#     assert solve_a(test_data) == 1928, solve_a(test_data)
# submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 2858, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
