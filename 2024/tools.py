# Usefull tools to sometimes use!
import re

adj4 = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
adj8 = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def nums(str, separator=None):
    if separator is None:
        result = []
        rx = r"-?\d+"
        for match in re.findall(rx, str):
            try:
                result.append(int(match))
            except:
                print("WARN: Cast failed")
        return result
    else:
        return list(map(int, str.strip().split(separator)))


def valPos(r, c, R, C):
    return r in range(R) and c in range(C)


def grid(input):
    input = input.strip().split("\n")
    R, C = len(input), len(input[0])

    return [list(x) for x in input], R, C


def fgrid(grid, target):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                return (r, c)

    return None
