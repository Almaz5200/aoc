import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 12
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    return grid(raw_data)


def solve_a(raw_data):
    data, R, C = prep_data(raw_data)

    seen = set()

    def srch(r, c):
        if (r, c) in seen:
            return 0, 0

        seen.add((r, c))

        ar = 1
        per = 0

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if not valPos(nr, nc, R, C) or data[nr][nc] != data[r][c]:
                per += 1
            if valPos(nr, nc, R, C) and data[nr][nc] == data[r][c]:
                a, b = srch(nr, nc)
                ar += a
                per += b

        return ar, per

    ans = 0

    for r in range(R):
        for c in range(C):
            a, b = srch(r, c)
            ans += a * b

    return ans


def solve_b(raw_data):
    data, R, C = prep_data(raw_data)

    seen = set()

    def srch(r, c, lseen):
        if (r, c) in seen:
            return 0

        seen.add((r, c))
        lseen.add((r, c))

        ar = 1

        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            # if not valPos(nr, nc, R, C) or data[nr][nc] == data[r][c]:
            #     if dr == 0:
            #         vsides.add((nc, dc))
            #     if nr == 0:
            #         hsides.add((nr, dr))
            if valPos(nr, nc, R, C) and data[nr][nc] == data[r][c]:
                a = srch(nr, nc, lseen)
                ar += a

        return ar

    # def perim()

    ans = 0

    def other(r, c, nr, nc):
        if not valPos(nr, nc, R, C) or data[nr][nc] != data[r][c]:
            return True
        return False

    for r in range(R):
        for c in range(C):
            sa = set()

            area = srch(r, c, sa)

            items = list(sa)
            if not items:
                continue
            Q = deque([items[0]])

            per = 0

            S = set()
            while Q:
                rr, cc = Q.popleft()
                S.add((rr, cc))

                for drr, dc in adj4:
                    nrr, nc = rr + drr, cc + dc
                    if rr == 0 and cc == 3:
                        print(nrr, nc)

                    if other(rr, cc, nrr, nc):
                        if ((rr + dc, cc + drr) not in sa) or (
                            (rr + dc + drr, cc + dc + drr) in sa
                        ):
                            per += 1

                    if not other(rr, cc, nrr, nc) and (nrr, nc) not in S:
                        S.add((nrr, nc))
                        Q.append((nrr, nc))

            print(area, per, data[r][c])
            ans += area * per

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == 1930, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 1206, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
