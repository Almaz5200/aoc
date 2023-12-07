import os
import math
import sys
from typing import List
from aocd import get_data, submit

lines = get_data(day=6, year=2023)

pointsWon = 0

# with open(os.path.join(sys.path[0], "input.txt")) as f:
#     lines = f.read()


def parse_input(s):
    lines = s.splitlines()
    times = lines[0].split()[1:]
    times = [int(x) for x in times if x.isnumeric()]
    distances = lines[1].split()[1:]
    distances = [int(x) for x in distances if x.isnumeric()]

    tog = zip(times, distances)
    return [{"time": t, "distance": d} for t, d in tog]


def parse_inputb(s):
    lines = s.splitlines()
    times = lines[0].split()[1:]
    times = [x for x in times if x.isnumeric()]
    time = "".join(times)
    time = int(time)

    distances = lines[1].split()[1:]
    distances = [x for x in distances if x.isnumeric()]
    distance = "".join(distances)
    distance = int(distance)

    # return {time, distance}
    return [{"time": time, "distance": distance}]


def solve_a(data):
    ways = 1
    for race in data:
        t = race["time"]
        d = race["distance"] + 0.001

        le = math.ceil((t - math.sqrt(t**2 - 4 * d)) / 2)
        re = math.floor((t + math.sqrt(t**2 - 4 * d)) / 2)

        print(le, re)

        localways = re - le + 1
        print(localways)
        ways *= localways

    return ways


data = parse_input(lines)

datab = parse_inputb(lines)
print(solve_a(datab))
submit(solve_a(data), part="a", day=6, year=2023)
submit(solve_a(datab), part="b", day=6, year=2023)
