import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 20
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ms = []
    for line in s.splitlines():
        k = line.split(" -> ")
        ds = k[1].split(", ")
        mt, mn = "", ""
        if k[0] == "broadcaster":
            mt = "b"
            mn = "broadcaster"
        else:
            mt = k[0][0]
            mn = k[0][1:]

        ms.append((mt, mn, ds))

    return ms


def solve_a(data):
    Q = deque([])
    names = [x[1] for x in data]

    S = {}

    for d in data:
        t, n, s = d
        if t == "%":
            S[n] = False
        if t == "&":
            S[n] = {}
            for src in data:
                _, nm, dsts = src
                if n in dsts:
                    S[n][nm] = 0

    lows, highs = 0, 0
    for _ in range(1000):
        Q.append(("button", 0, "broadcaster"))
        while Q:
            src, f, dst = Q.popleft()

            if f == 0:
                lows += 1
            elif f == 1:
                highs += 1

            try:
                dstm = data[names.index(dst)]
            except:
                continue

            dstt, dstn, dsts = dstm

            if dstt == "b":
                for d in dsts:
                    Q.append((dstn, f, d))

            if dstt == "%":
                if f == 0:
                    if S[dstn] is False:
                        S[dstn] = True
                        for d in dsts:
                            Q.append((dstn, 1, d))
                    else:
                        S[dstn] = False
                        for d in dsts:
                            Q.append((dstn, 0, d))

            if dstt == "&":
                S[dstn][src] = f
                if all(S[dstn].values()):
                    for d in dsts:
                        Q.append((dstn, 0, d))
                else:
                    for d in dsts:
                        Q.append((dstn, 1, d))

    return lows * highs


def solve_b(data):
    Q = deque([])
    names = [x[1] for x in data]

    S = {}

    for d in data:
        t, n, s = d
        if t == "%":
            S[n] = False
        if t == "&":
            S[n] = {}
            for src in data:
                _, nm, dsts = src
                if n in dsts:
                    S[n][nm] = 0

    lows, highs = 0, 0
    rms = defaultdict(list)
    for i in range(10000000000):
        Q.append(("button", 0, "broadcaster"))
        while Q:
            src, f, dst = Q.popleft()

            if f == 0:
                if dst == "rx":
                    return i + 1
                lows += 1
            elif f == 1:
                highs += 1

            try:
                dstm = data[names.index(dst)]
            except:
                continue

            dstt, dstn, dsts = dstm

            if dstt == "b":
                for d in dsts:
                    Q.append((dstn, f, d))

            if dstt == "%":
                if f == 0:
                    if S[dstn] is False:
                        S[dstn] = True
                        for d in dsts:
                            Q.append((dstn, 1, d))
                    else:
                        S[dstn] = False
                        for d in dsts:
                            Q.append((dstn, 0, d))

            if dstt == "&":
                S[dstn][src] = f
                if all(S[dstn].values()):
                    if dstn in ["st", "gr", "bn", "lg"]:
                        rms[dstn].append(i)
                    for d in dsts:
                        Q.append((dstn, 0, d))
                else:
                    for d in dsts:
                        Q.append((dstn, 1, d))
        # I didn't realize you could just take lcm, so i took those values and just solved chinese remainder theorem with them using online calculator
        if i % 50000 == 0:
            for k in rms:
                print(k, rms[k][-1], rms[k][-1] - rms[k][-2])


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 11687500, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

submit(solve_b(data), part="b", day=day, year=2023)
