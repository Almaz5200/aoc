import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid, Grid

day = 22
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)

MOD = 16777216


def prep_data(raw_data):
    # return raw_data.strip()
    return nums(raw_data)


def tsznd(num):
    res = num
    for _ in range(2000):
        tmp = res * 64
        res ^= tmp
        res %= MOD
        tmp = res // 32
        res ^= tmp
        res %= MOD
        tmp = res * 2048
        res ^= tmp
        res %= MOD
    return res


def solve_a(raw_data):
    data = prep_data(raw_data)
    ans = 0
    for d in data:
        ans += tsznd(d)

    return ans


def solve_b(raw_data):
    data = prep_data(raw_data)

    D = defaultdict(lambda: defaultdict(int))

    for i, num in enumerate(data):
        l4changes = []
        res = num
        prres = res
        for _ in range(2000):
            tmp = res * 64
            res ^= tmp
            res %= MOD
            tmp = res // 32
            res ^= tmp
            res %= MOD
            tmp = res * 2048
            res ^= tmp
            res %= MOD
            l4changes.append(res % 10 - prres % 10)
            prres = res
            # print(l4changes[-1])
            if len(l4changes) > 4:
                l4changes = l4changes[1:]

            if len(l4changes) == 4:
                ky = (
                    l4changes[0],
                    l4changes[1],
                    l4changes[2],
                    l4changes[3],
                )
                # if ky == (-2, 1, -1, 3):
                #     print(ky)
                if i not in D[ky]:
                    D[ky][i] = res % 10

    ans = 0
    for k, v in D.items():
        mx = sum(v.values())
        # if mx == 25:
        #     print(k)
        #     print(v)
        if k == (-2, 1, -1, 3):
            print(k, v)
        ans = max(ans, mx)

    return ans


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

# if test_data:
#     assert solve_a(test_data) == 37327623, solve_a(test_data)
# submit(solve_a(lines), part="a", day=day, year=2024)

if test_data:
    assert solve_b(test_data) == 23, solve_b(test_data)
submit(solve_b(lines), part="b", day=day, year=2024)
