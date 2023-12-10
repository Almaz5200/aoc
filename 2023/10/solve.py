import os
import math
import sys
from typing import List
from aocd import get_data, submit

day = 10
lines = get_data(day=day, year=2023)

sys.setrecursionlimit(100000000)


def parse_input(s):
    ll = s.splitlines()
    map = []
    starting = (0, 0)

    for i in range(len(ll)):
        map.append([])
        for j in range(len(ll[i])):
            if ll[i][j] == "|":
                map[i].append([(i - 1, j), (i + 1, j)])
            elif ll[i][j] == "-":
                map[i].append([(i, j - 1), (i, j + 1)])
            elif ll[i][j] == "L":
                map[i].append([(i - 1, j), (i, j + 1)])
            elif ll[i][j] == "J":
                map[i].append([(i, j - 1), (i - 1, j)])
            elif ll[i][j] == "7":
                map[i].append([(i, j - 1), (i + 1, j)])
            elif ll[i][j] == "F":
                map[i].append([(i + 1, j), (i, j + 1)])
            elif ll[i][j] == "S":
                starting = (i, j)
                map[i].append([])
            else:
                map[i].append([])

    return map, starting


def walk(map, current, prev, depth):
    if map[current[0]][current[1]] == []:
        return depth

    for di in map[current[0]][current[1]]:
        if di == prev:
            continue
        return walk(map, di, current, depth + 1)


def solve_a(data):
    m, s = data

    start = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if s in m[i][j]:
                start = (i, j)
                break
        if start is not None:
            break

    return walk(m, start, s, 1) // 2


def walk_b(map, current, prevs, depth):
    if map[current[0]][current[1]] == []:
        return depth, [current] + prevs

    for di in map[current[0]][current[1]]:
        if di in prevs:
            continue
        return walk_b(map, di, prevs + [current], depth + 1)

    return depth, [current] + prevs


def paint(m, loop, current, prevs, confs):
    if current in prevs:
        return confs

    if current == (1, 1):
        print("DICK", m[current[0]][current[1]])
    for di in m[current[0]][current[1]]:
        if di in prevs:
            continue
        offset = (di[0] - current[0], di[1] - current[1])
        if offset == (-1, 0):
            for i, j in [
                (current[0] - 1, current[1] + 1),
                (current[0], current[1] + 1),
            ]:
                if (i, j) not in loop:
                    confs[(i, j)] = True
        elif offset == (0, 1):
            for i, j in [
                (current[0] + 1, current[1] + 1),
                (current[0] + 1, current[1]),
            ]:
                if (i, j) not in loop:
                    confs[(i, j)] = True
        elif offset == (1, 0):
            for i, j in [
                (current[0] + 1, current[1] - 1),
                (current[0], current[1] - 1),
            ]:
                if (i, j) not in loop:
                    confs[(i, j)] = True

        elif offset == (0, -1):
            for i, j in [
                (current[0] - 1, current[1] - 1),
                (current[0] - 1, current[1]),
            ]:
                if (i, j) not in loop:
                    confs[(i, j)] = True

        return paint(m, loop, di, prevs + [current], confs)

    return confs


def expand(current, prevs, loop, confs):
    if current in prevs:
        return confs
    for di in [
        (current[0] - 1, current[1]),
        (current[0], current[1] + 1),
        (current[0] + 1, current[1]),
        (current[0], current[1] - 1),
    ]:
        if di in prevs:
            continue
        if di in loop:
            continue
        if di in confs:
            continue
        confs[di] = True
        confs = expand(di, prevs + [current], loop, confs)
    return confs


def solve_b(data):
    m, s = data
    start = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if s in m[i][j]:
                start = (i, j)
                break
        if start is not None:
            break

    ln, loop = walk_b(m, start, [s], 1)

    print(m[s[0]][s[1]])
    m[s[0]][s[1]] = [loop[0], loop[2]]

    confs = {}
    # walk right edge. That's not guaranteed to work, i've just checked that my loop touches it
    for i in range(len(m)):
        if (i, len(m[i]) - 1) in loop and (i - 1, len(m[i]) - 1) in loop:
            confs = paint(m, loop, (i, len(m[i]) - 1), [(i - 1, len(m[i]) - 1)], {})

    ogConfs = confs.copy()
    for c in ogConfs:
        confs = expand(c, [], loop, confs)

    return len(confs)


data = parse_input(lines)

with open("input.txt", "r") as f:
    test_data = parse_input(f.read())

assert solve_a(test_data) == 24, solve_a(test_data)
submit(solve_a(data), part="a", day=day, year=2023)

assert solve_b(test_data) == 5
submit(solve_b(data), part="b", day=day, year=2023)
