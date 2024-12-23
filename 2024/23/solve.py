import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid, Grid
import networkx as nx

day = 23
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    d = raw_data.strip().split("\n")
    return [x.split("-") for x in d]
    # return Grid(raw_data)


def solve_a(raw_data):
    data = prep_data(raw_data)
    print(len(data))

    ADJ = defaultdict(set)

    comps = set()
    for a, b in data:
        comps.add(a)
        comps.add(b)
        ADJ[a].add(b)
        ADJ[b].add(a)
    print(len(comps))

    ans = set()

    for a in comps:
        for b in comps:
            for c in comps:
                if a == b or a == c or b == c:
                    continue

                if (
                    not a.startswith("t")
                    and not b.startswith("t")
                    and not c.startswith("t")
                ):
                    continue

                if b in ADJ[a] and c in ADJ[a] and c in ADJ[b]:
                    s = sorted((a, b, c))
                    k = (s[0], s[1], s[2])
                    if k not in ans:
                        ans.add((s[0], s[1], s[2]))
                        # print(s)

    return len(ans)


def solve_b(raw_data):
    data = prep_data(raw_data)

    ADJ = defaultdict(list)

    comps = set()
    for a, b in data:
        comps.add(a)
        comps.add(b)
        ADJ[a].append(b)
        ADJ[b].append(a)
    print(len(comps))

    g = nx.from_dict_of_lists(ADJ)

    ans = []
    for c in nx.find_cliques(g):
        if len(c) > len(ans):
            ans = c

    # print(",".join(sorted(list(ans))))
    return ",".join(sorted(list(ans)))


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

# if test_data:
#     assert solve_a(test_data) == 7, solve_a(test_data)
# submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == "co,de,ka,ta", solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
