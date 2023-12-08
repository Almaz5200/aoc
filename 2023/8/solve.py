import os
import math
import sys
from typing import List
from aocd import get_data, submit

day = 8
lines = get_data(day=day, year=2023)


def parse_input(s: str):
    a = s.split("\n\n")
    instruct = a[0]

    lines = a[1].splitlines()
    lines = [line.split(" = ") for line in lines]
    lines = [(line[0], line[1][1:-1]) for line in lines]
    lines = [
        (line[0], line[1].split(", ")[0], line[1].split(", ")[1]) for line in lines
    ]

    dict = {}
    for line in lines:
        dict[line[0]] = (line[1], line[2])

    return (instruct, dict)


# weird to assume that cycle always ens with a Z and goes back to A, but it worked
def solve(data, p2=False):
    guide = data[0]
    map = data[1]

    steps = 0
    currents = []
    for element in map.keys():
        if element.endswith("A" if p2 else "AAA"):
            currents.append(element)
            print("Added", element)

    cycles = {}

    for i, current in enumerate(currents):
        cycles[i] = (-1, [current])

    while True:
        for i, current in enumerate(currents):
            currents[i] = map[current][guide[steps % len(guide)] == "R"]
            if currents[i].endswith("Z"):
                if cycles[i][0] == -1:
                    cycles[i] = (
                        0,
                        cycles[i][1],
                    )
                continue

            if cycles[i][0] == -1:
                cycles[i][1].append(currents[i])

        steps += 1

        hasNonZ = False
        for cycle in cycles.values():
            if cycle[0] == -1:
                hasNonZ = True

        if not hasNonZ:
            break

    lens = []
    for i in range(len(cycles)):
        lens.append(len(cycles[i][1]))

    lcm = 1
    for lm in lens:
        lcm = math.lcm(lm, lcm)

    return lcm


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve(test_data) == 6, solve(test_data)
submit(solve(data), part="a", day=day, year=2023)

with open("input_b.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve(test_data, p2=True) == 6, solve(test_data, p2=True)
submit(solve(data, p2=True), part="b", day=day, year=2023)
