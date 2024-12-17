import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
import z3
from ..tools import adj4, adj8, nums, valPos, grid, fgrid

day = 17
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    d = raw_data.strip().split("\n")
    a, b, c = nums(",".join(d[:3]))
    i = nums(d[-1])
    return a, b, c, i


def solve_a(raw_data):
    a, b, c, inst = prep_data(raw_data)

    print(a, b, c, inst)

    ans = []

    def value(arg):
        if arg <= 3:
            return arg
        elif arg == 4:
            return a
        elif arg == 5:
            return b
        elif arg == 6:
            return c
        assert False

    i = 0
    while i < len(inst):
        op = inst[i]
        arg = inst[i + 1]
        argVal = value(arg)
        if op == 0:
            a = a // (2**argVal)
        elif op == 1:
            b = b ^ arg
        elif op == 2:
            b = argVal % 8
        elif op == 3:
            if a != 0:
                i = arg
                continue
        elif op == 4:
            b = b ^ c
        elif op == 5:
            ans.append(argVal % 8)
        elif op == 6:
            b = a // (2**argVal)
        elif op == 7:
            c = a // (2**argVal)
        i += 2

    return ",".join([str(x) for x in ans])


def solve_b(raw_data):
    oa, ob, oc, inst = prep_data(raw_data)

    def getDigit(pot):
        preb = (pot % 8) ^ 5
        return ((preb ^ 6) ^ (pot // (2**preb))) % 8

    candidates = {0}
    for i, n in enumerate(inst[::-1]):
        ans = 0
        ncan = set()
        for can in candidates:
            for new in range(8):
                if getDigit(can * 8 + new) == n:
                    ncan.add(can * 8 + new)

        candidates = ncan

    oa = min(candidates)

    a = oa
    b = ob
    c = oc
    ans = []

    def value(arg):
        if arg <= 3:
            return arg
        elif arg == 4:
            return a
        elif arg == 5:
            return b
        elif arg == 6:
            return c
        assert False

    i = 0
    while i < len(inst):
        op = inst[i]
        arg = inst[i + 1]
        argVal = value(arg)
        if op == 0:
            a = a // (2**argVal)
        elif op == 1:
            b = b ^ arg
        elif op == 2:
            b = argVal % 8
        elif op == 3:
            if a != 0:
                i = arg
                continue
        elif op == 4:
            b = b ^ c
        elif op == 5:
            print((a % 8) ^ 3 ^ (a // 2 ** ((a % 8) ^ 5)) % 8, argVal % 8)
            ans.append(argVal % 8)
        elif op == 6:
            b = a // (2**argVal)
        elif op == 7:
            c = a // (2**argVal)
        i += 2

    if ans == inst:
        return oa


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()

if test_data:
    assert solve_a(test_data) == "4,6,3,5,6,3,5,2,1,0", solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)
submit(solve_b(lines), part="b", day=day, year=2024)
