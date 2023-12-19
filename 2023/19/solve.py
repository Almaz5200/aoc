import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict

from aocd.models import json

day = 19
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s
    ll = ll.split("\n\n")

    r, p = ll[0], ll[1]

    r = r.split("\n")
    ruls = []
    for rul in r:
        m = rul.split("{")
        name, r = m[0], m[1][:-1]

        r = r.split(",")

        wfs = []
        for w in r:
            k = w.split(":")
            if len(k) == 1:
                wfs.append(("x", True, -1, w))
                continue

            c = k[0]

            wfs.append((c[0], c[1] == ">", int(c[2:]), k[1]))

        ruls.append((name, wfs))

    ps = []
    for par in p.split("\n"):
        part = par
        part = part.replace("=", ":")
        part = part.replace("x", '"x"')
        part = part.replace("m", '"m"')
        part = part.replace("a", '"a"')
        part = part.replace("s", '"s"')
        if len(part) > 0:
            ps.append(json.loads(part))

    return (ruls, ps)


def solve_a(data):
    rules, parts = data

    rnames = [x[0] for x in rules]
    inInd = rnames.index("in")
    print(inInd)

    accParts = []
    for part in parts:
        cInd = inInd
        while True:
            if cInd == -1:
                break

            rl = rules[cInd]
            nm, wfs = rl

            for wf in wfs:
                c, gt, v, k = wf
                if (part[c] > v and gt) or (part[c] < v and not gt):
                    if k == "R":
                        cInd = -1
                        break

                    if k == "A":
                        accParts.append(part)
                        cInd = -1
                        break

                    cInd = rnames.index(k)
                    break
    sum_ = 0
    for part in accParts:
        sum_ += part["x"]
        sum_ += part["m"]
        sum_ += part["a"]
        sum_ += part["s"]

    return sum_


def calCombs(rules, partt, crule) -> int:
    def lenr(r):
        return r[1] - r[0]

    if crule == "R":
        return 0
    if crule == "A":
        return lenr(partt["x"]) * lenr(partt["m"]) * lenr(partt["a"]) * lenr(partt["s"])

    rnames = [x[0] for x in rules]

    part = copy.deepcopy(partt)
    tot = 0

    for wf in rules[rnames.index(crule)][1]:
        c, gt, v, k = wf
        ptl, ptm = part[c]

        if gt:
            nrl = max(v + 1, ptl)
            nrh = ptm
        else:
            nrl = ptl
            nrh = min(v, ptm)

        npart = copy.deepcopy(part)

        if nrl <= nrh:
            npart[c] = (nrl, nrh)
            tot += calCombs(rules, npart, k)

        cpart = copy.deepcopy(part)
        cpart[c] = (ptl, nrl) if gt else (nrh, ptm)

        print("separated into ", cpart, " and ", npart)

        if cpart[c][0] >= cpart[c][1]:
            print("breaking")
            break

        part = cpart

    return tot


def solve_b(data):
    rules, _ = data
    res = calCombs(
        rules, {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}, "in"
    )

    return res


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 19114, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 167409079868000, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
