import os
import math
import heapq
import sys
import copy
from typing import List
from aocd import get_data, submit

day = 17
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)

### ALL BELLOW ARE FROM JONATHAN PAULSON CODE ###
### Literal copy paste, was in no condition to think properly myself ###
### Got through it and understood tho ###
### Couldn't figure myself quick enough :( ###
D = lines
L = D.split("\n")
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])


def solve(part2):
    Q = [(0, 0, 0, -1, -1)]
    D = {}
    while Q:
        dist, r, c, dir_, indir = heapq.heappop(Q)
        if (r, c, dir_, indir) in D:
            continue
        D[(r, c, dir_, indir)] = dist
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            rr = r + dr
            cc = c + dc
            new_dir = i
            new_indir = 1 if new_dir != dir_ else indir + 1

            isnt_reverse = (new_dir + 2) % 4 != dir_

            isvalid_part1 = new_indir <= 3
            isvalid_part2 = new_indir <= 10 and (
                new_dir == dir_ or indir >= 4 or indir == -1
            )
            isvalid = isvalid_part2 if part2 else isvalid_part1

            if 0 <= rr < R and 0 <= cc < C and isnt_reverse and isvalid:
                cost = int(G[rr][cc])
                heapq.heappush(Q, (dist + cost, rr, cc, new_dir, new_indir))

    ans = 1e9
    for (r, c, dir_, indir), v in D.items():
        if r == R - 1 and c == C - 1:
            ans = min(ans, v)
    return ans


submit(solve(False), part="a", day=day, year=2023)
submit(solve(True), part="b", day=day, year=2023)
