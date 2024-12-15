import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 15
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return grid(raw_data.split("\n\n")[0]), [
        x for x in raw_data.split("\n\n")[1].strip() if x != "\n"
    ]


def solve_a(raw_data):
    (data, R, C), moves = prep_data(raw_data)
    ans = 0
    fpos = fgrid(data, "@")

    if not fpos:
        return -1

    dirs = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
    }

    for move in moves:
        dir = dirs[move]

        pr, pc = fpos[0] + dir[0], fpos[1] + dir[1]
        nr, nc = pr, pc

        while valPos(pr, pc, R, C) and data[pr][pc] == "O":
            pr, pc = pr + dir[0], pc + dir[1]

        if not valPos(pr, pc, R, C) or data[pr][pc] == "#":
            continue

        data[pr][pc] = "O"
        data[nr][nc] = "@"
        data[fpos[0]][fpos[1]] = " "

        fpos = (nr, nc)

    ans = 0
    for r in range(R):
        for c in range(C):
            if data[r][c] == "O":
                ans += 100 * r + c

    return ans


def solve_b(raw_data: str):
    raw_data = raw_data.replace(
        "#",
        "##",
    )
    raw_data = raw_data.replace(
        "O",
        "[]",
    )
    raw_data = raw_data.replace(
        ".",
        "..",
    )
    raw_data = raw_data.replace("@", "@.")

    (data, R, C), moves = prep_data(raw_data)
    ans = 0
    fpos = fgrid(data, "@")

    if not fpos:
        return -1

    dirs = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
    }
    # for r in data:
    #     print(r)
    # print("START")

    def canMove(r, c, dir, should):
        if data[r][c] == ".":
            return True
        if data[r][c] == "#":
            return False

        if data[r][c] == "]":
            return canMove(r, c - 1, dir, should)

        nr, nc = r + dir[0], c + dir[1]

        if data[nr][nc] == "#" or data[nr][nc + 1] == "#":
            return False
        # if data[nr][nc] == "." and data[nr][nc] == ".":
        #     return False

        can = True
        if not data[nr][nc] == ".":
            if data[nr][nc] == "[":
                can = canMove(nr, nc, dir, should)
            else:
                can = canMove(nr, nc - 1, dir, should)

        if not data[nr][nc + 1] == ".":
            if data[nr][nc + 1] == "[":
                can = can and canMove(nr, nc + 1, dir, should)

        if can and should:
            data[nr][nc] = data[r][c]
            data[nr][nc + 1] = data[r][c + 1]
            data[r][c] = "."
            data[r][c + 1] = "."

        return can

    for move in moves:
        dir = dirs[move]
        odata = copy.deepcopy(data)
        # print("===")
        # print(move)

        if dir[1] != 0:
            pr, pc = fpos[0] + dir[0], fpos[1] + dir[1]
            nr, nc = pr, pc

            while valPos(pr, pc, R, C) and data[pr][pc] in ["[", "]"]:
                if data[pr][pc] == "[":
                    data[pr][pc] = "]"
                elif data[pr][pc] == "]":
                    data[pr][pc] = "["
                pr, pc = pr + dir[0], pc + dir[1]

            if not valPos(pr, pc, R, C) or data[pr][pc] == "#":
                data = odata
                continue

            a, b = pc, nc
            if a > b:
                a, b = b, a

            # for i in range(a, b + 1):
            #     if data[nr][i] == "[":
            #         data[nr][i] = "]"
            #     if data[nr][i] == "]":
            #         data[nr][i] = "["

            if dir[1] == 1:
                data[pr][pc] = "]"
            else:
                data[pr][pc] = "["
            # if dir[1] == 1:
            #     data[pr][pc] = "]"
            #     data[pr][pc - dir[1]] = "["
            # else:
            #     data[pr][pc] = "["
            #     data[pr][pc - dir[1]] = "]"
            data[nr][nc] = "@"
            data[fpos[0]][fpos[1]] = "."

            fpos = (nr, nc)

        else:
            # for r in data:
            #     print(r)
            # print("EX")
            if not canMove(fpos[0] + dir[0], fpos[1] + dir[1], dir, False):
                continue
            canMove(fpos[0] + dir[0], fpos[1] + dir[1], dir, True)
            data[fpos[0] + dir[0]][fpos[1] + dir[1]] = "@"
            data[fpos[0]][fpos[1]] = "."
            fpos = (fpos[0] + dir[0], fpos[1] + dir[1])

        # for r in data:
        #     print(r)
        # print("===")

    ans = 0
    for r in range(R):
        for c in range(C):
            if data[r][c] == "[":
                ans += 100 * r + c

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 10092, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 9021, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
