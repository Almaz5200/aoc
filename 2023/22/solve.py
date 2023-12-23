import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 22
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)

# My solution is insanely slow, but it works and I'm too lazy to optimize it for now


def parse_input(s):
    brs = []
    for line in s.splitlines():
        sp = line.split("~")
        st, en = sp[0], sp[1]
        st = st.split(",")
        en = en.split(",")
        st = [int(x) for x in st]
        en = [int(x) for x in en]
        brs.append(((st[0], st[1], st[2]), (en[0], en[1], en[2])))

    return brs


def contains_point(br, p):
    (xs, ys, zs), (xe, ye, ze) = br
    x, y, z = p
    return xs <= x <= xe and ys <= y <= ye and zs <= z <= ze


def fall_each(brs, justcheck=False, droppeds=(set([]))):
    didFall = False
    for i, br in enumerate(brs):
        (xs, ys, zs), (xe, ye, ze) = br
        minz = min(zs, ze)
        if minz == 1 or (justcheck and didFall):
            continue

        pts = []
        for x in range(xs, xe + 1):
            for y in range(ys, ye + 1):
                pts.append((x, y, minz - 1))

        has_sup = False
        for bra in brs:
            if has_sup:
                break
            for p in pts:
                if contains_point(bra, p):
                    has_sup = True
                    break

        if not has_sup:
            didFall = True
            brs[i] = ((xs, ys, zs - 1), (xe, ye, ze - 1))
            droppeds.add(i)

    return brs, didFall, droppeds


def solve_a(data):
    dat = copy.deepcopy(data)
    i = 0
    while True:
        ndat, didFall, droppeds = fall_each(dat)
        dat = ndat

        i += 1
        print(f"Falling {i}th time")

        if not didFall:
            break
    print("Finish fall")

    canDrop = 0
    for i, br in enumerate(dat):
        hyp = copy.deepcopy(dat)
        hyp.pop(i)
        _, didFall, _ = fall_each(hyp, justcheck=True)
        if not didFall:
            canDrop += 1

    return canDrop


def solve_b(data):
    dat = copy.deepcopy(data)
    i = 0
    while True:
        ndat, didFall, droppeds = fall_each(dat)
        dat = ndat

        i += 1
        print(f"Falling {i}th time")

        if not didFall:
            break
    print("Finish fall")

    drupNum = 0
    for i, br in enumerate(dat):
        print(f"Checking {i}th brick out of {len(dat)}")
        hyp = copy.deepcopy(dat)
        hyp.pop(i)
        droppeds = set()
        while True:
            _, didFall, droppeds = fall_each(
                hyp,
                justcheck=True,
                droppeds=droppeds,
            )
            if not didFall:
                break
        drupNum += len(droppeds)

    return drupNum


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

# assert solve_a(test_data) == 5, solve_a(test_data)
# submit(solve_a(data), part="a", day=day, year=2023)
assert solve_b(test_data) == 7, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
