import os
import math
import sys
import networkx as nx
import copy
from typing import List
from aocd import get_data, submit
from collections import defaultdict, deque

from aocd.models import json

day = 25
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    res = defaultdict(list)
    for line in s.splitlines():
        sd = line.split(": ")
        src = sd[0]
        trgs = sd[1].split()
        for trg in trgs:
            res[src].append(trg)
            # res[trg].append(src)
    return res


def solve_a(data):
    graph = nx.DiGraph()
    for src, trgs in data.items():
        for trg in trgs:
            graph.add_edge(src, trg, capacity=1)
            graph.add_edge(trg, src, capacity=1)

    # present it
    for node in graph.nodes:
        print(node, graph[node])

    part = ()
    for x in range(len(data)):
        for y in range(len(data), 0, -1):
            if x == y:
                continue
            ks = list(data.keys())
            cut_value, partition = nx.minimum_cut(graph, ks[x], ks[y])
            if cut_value == 3:
                part = partition
                break
    cum = 1
    for p in part:
        cum *= len(p)

    return cum


def solve_b(data):
    return 0


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 54, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == -1, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
