import os
import math
import sys
import copy
from typing import List
from aocd import get_data, submit

day = 15
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    s = s.replace("\n", "")
    return s.split(",")


def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def solve_a(data):
    sumd = 0
    print(hash("HASH"))

    for d in data:
        print("d is", d, hash(d))
        sumd += hash(d)

    return sumd


def solve_b(data):
    boxes = [[] for _ in range(256)]

    for d in data:
        if "-" in d:
            label = d[:-1]
            bx = hash(label)
            for i, lens in enumerate(boxes[bx]):
                if lens["lb"] == label:
                    boxes[bx].pop(i)
                    break
        else:
            label = d.split("=")[0]
            length = int(d.split("=")[1])
            bx = hash(label)
            didFind = False
            for i, lens in enumerate(boxes[bx]):
                if lens["lb"] == label:
                    boxes[bx][i]["ln"] = length
                    didFind = True
                    break
            if not didFind:
                boxes[bx].append({"lb": label, "ln": length})

    total = 0
    for i, box in enumerate(boxes):
        num = i + 1
        for ind, lens in enumerate(box):
            total += lens["ln"] * num * (ind + 1)

    return total


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 1320, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 145, solve_b(test_data)
submit(solve_b(data), part="b", day=day, year=2023)
