from functools import lru_cache
import os
import math
import itertools
import random
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque, Counter
import re
from ..tools import adj4, adj8, nums, valPos, grid, fgrid, Grid

day = 24
lines = get_data(day=day, year=2024)

sys.setrecursionlimit(100000000)


def prep_data(raw_data):
    # return raw_data.strip()
    a, b = raw_data.split("\n\n")
    R = {}
    for l in a.split("\n"):
        reg, val = l.split(": ")
        val = True if int(val) == 1 else False
        R[reg] = val

    insts = []

    for inst in b.strip().split("\n"):
        m, tar = inst.split(" -> ")
        i, j, k = m.split(" ")
        insts.append((i, j, k, tar))

    return R, insts


class Node:
    op: str
    in1: str
    in2: str


def solve_a(raw_data):
    R, insts = prep_data(raw_data)
    ans = 0

    ns = {}
    for a, op, b, tar in insts:
        ns[tar] = Node()
        ns[tar].in1 = a
        ns[tar].in2 = b
        ns[tar].op = op

    @lru_cache(maxsize=None)
    def resolve(val):
        if val in R:
            return R[val]
        node = ns[val]
        aval = resolve(node.in1)
        bval = resolve(node.in2)
        op = node.op

        if op == "AND":
            return aval and bval
        elif op == "OR":
            return aval or bval
        elif op == "XOR":
            return aval != bval

    for _, _, _, tar in insts:
        if tar.startswith("z"):
            order = int(tar[1:])
            if resolve(tar):
                ans += 2**order

    return ans


def solve_b(raw_data, swp):
    R, insts = prep_data(raw_data)

    ns = {}

    for a, op, b, tar in insts:
        ns[tar] = Node()
        ns[tar].in1 = a
        ns[tar].in2 = b
        ns[tar].op = op

    T = set()

    def resolve(val):
        T.add(val)
        if val in R:
            return R[val]
        node = ns[val]
        aval = resolve(node.in1)
        bval = resolve(node.in2)
        op = node.op

        if op == "AND":
            return aval and bval
        elif op == "OR":
            return aval or bval
        elif op == "XOR":
            return aval != bval

    def branch_lines(node_id):
        if node_id in R:
            return [node_id]

        node = ns[node_id]

        lines = [f"{node_id} ==OP== {node.op}"]
        for l in branch_lines(node.in1):
            lines.append("  " + l)
        for l in branch_lines(node.in2):
            lines.append("  " + l)

        return lines

    bad_nodes = set()

    def fill():
        for k in R.keys():
            R[k] = random.choice([True, False])

    def swap(a, b):
        ns[a], ns[b] = ns[b], ns[a]

    ## hand picked with code bellow
    swap("z39", "tnc")
    swap("fsq", "dvb")
    swap("z10", "vcf")
    swap("z17", "fhg")

    for _ in range(10):
        fill()
        xnum, ynum = 0, 0
        for k, v in R.items():
            if k.startswith("x"):
                order = int(k[1:])
                if resolve(k):
                    xnum += 2**order
        for k, v in R.items():
            if k.startswith("y"):
                order = int(k[1:])
                if resolve(k):
                    ynum += 2**order

        correctAns = []
        correctInt = xnum + ynum
        for _ in range(46):
            correctAns.append(correctInt % 2 == 1)
            correctInt //= 2

        # correctAns = correctAns[::-1]
        # print(correctAns)

        for num in range(46):
            if resolve(f"z{str(num).zfill(2)}") != correctAns[num]:
                bad_nodes.add(f"z{str(num).zfill(2)}")

    print(bad_nodes)
    for node in bad_nodes:
        for l in branch_lines(node):
            if l.startswith("              "):
                continue
            print(l)

    ## example
    for l in branch_lines("z07"):
        if l.startswith("              "):
            continue
        print(l)

    print(",".join(sorted(["z39", "tnc", "fsq", "dvb", "z10", "vcf", "z17", "fhg"])))

    assert False

    return ""


with open(f"2024/{day}/test_input.txt", "r") as f:
    test_data = f.read()


# if test_data:
#     assert solve_a(test_data) == 2024, solve_a(test_data)
submit(solve_a(lines), part="a", day=day, year=2024)

solve_b(lines, 8)
# if test_data:
#     assert solve_b(test_data, 4) == "z00,z01,z02,z05", solve_b(test_data, 4)
# submit(solve_b(lines, 8), part="b", day=day, year=2024)
