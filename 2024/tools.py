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


"""
Deprecated, use Grid class
"""


def grid(input):
    input = input.strip().split("\n")
    R, C = len(input), len(input[0])

    return [list(x) for x in input], R, C


class Grid:
    def __init__(self, input):
        input = input.strip().split("\n")
        self.data = input
        self.R, self.C = len(input), len(input[0])
        self.walls = []

    def __iter__(self):
        for r in range(self.R):
            for c in range(self.C):
                yield (r, c), self.data[r][c]

    def __getitem__(self, key):
        if isinstance(key, tuple):
            r, c = key
            return self.data[r][c]
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            r, c = key
            self.data[r][c] = value
        else:
            self.data[key] = value

    def adj4(self, pos):
        r, c = pos
        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if valPos(nr, nc, self.R, self.C) and self[(nr, nc)] not in self.walls:
                yield (nr, nc), self[(nr, nc)]

    def dirAdj4(self, pos):
        r, c = pos
        for dr, dc in adj4:
            nr, nc = r + dr, c + dc
            if valPos(nr, nc, self.R, self.C) and self[(nr, nc)] not in self.walls:
                yield (dr,dc), (nr, nc), self[(nr, nc)]

    def adj8(self, pos):
        r, c = pos
        for dr, dc in adj8:
            nr, nc = r + dr, c + dc
            if valPos(nr, nc, self.R, self.C) and self[(nr, nc)] not in self.walls:
                yield (nr, nc), self[(nr, nc)]

    def find(self, target):
        for pos, value in self:
            if value == target:
                return pos
        return None


def fgrid(grid, target):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                return (r, c)

    return None
