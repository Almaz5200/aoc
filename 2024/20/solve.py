import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 20
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return grid(raw_data)


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)
    sp = fgrid(data, "S")
    ep = fgrid(data, "E")

    D = {}

    Q = deque([(0, ep)])
    S = set([ep])
    while Q:
        cost, (r, c) = Q.popleft()

        D[(r, c)] = cost

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if data[nr][nc] != "#" and ((nr, nc) not in S):
                Q.append((cost + 1, (nr, nc)))
                S.add((nr, nc))

    Q = deque([(0, sp)])
    S = set([sp])
    ans = 0
    CC = defaultdict(int)
    while Q:
        cost, (r, c) = Q.popleft()

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if data[nr][nc] != "#" and ((nr, nc) not in S):
                Q.append((cost + 1, (nr, nc)))
                S.add((nr, nc))

            for ndr, ndc in adj4:
                cnr, cnc = nr + ndr, nc + ndc
                if valPos(cnr, cnc, R, C) and data[cnr][cnc] != "#":
                    benefit = D[(r, c)] - D[(cnr, cnc)] - 2
                    if benefit == 4:
                        print(r, c, cnr, cnc)
                    if (benefit) > 0:
                        # print(benefit)
                        CC[benefit] += 1
                    if benefit >= 100:
                        ans += 1

    for k, v in CC.items():
        print(k, v)

    return ans


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)
    sp = fgrid(data, "S")
    ep = fgrid(data, "E")

    D = {}

    Q = deque([(0, ep)])
    S = set([ep])
    while Q:
        cost, (r, c) = Q.popleft()

        D[(r, c)] = cost

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if data[nr][nc] != "#" and ((nr, nc) not in S):
                Q.append((cost + 1, (nr, nc)))
                S.add((nr, nc))

    print("Regular cost", D[sp])

    ans = 0

    for r in range(R):
        print(r)
        for c in range(C):
            if data[r][c] == "#":
                continue
            for tr in range(r - 21, r + 21):
                for tc in range(c - 21, c + 21):
                    if not valPos(tr, tc, R, C):
                        continue
                    if data[tr][tc] == "#":
                        continue

                    p = abs(tr - r) + abs(tc - c)
                    if p > 20:
                        continue

                    win = D[(r, c)] - (p + D[(tr, tc)])

                    if win >= 100:
                        ans += 1
    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

# if test_data:
#     assert solve_a(test_data) == 2, solve_a(test_data)
# submit(solve_a(lines), part="a", day=day, year=2024)

# if test_data:
#     assert solve_b(test_data) != 0, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
