import os
import sys
from typing import List

with open("input.txt") as f:
    lines = f.readlines()

isDone: List[List[bool]] = []
map: List[List[int]] = []


def getLine(i, j):
    if i < 0 or i > len(map):
        return None
    if j < 0 or j > len(map[i]):
        return None

    if map[i][j] == -2:
        return None
    ci, cj = i, j
    while True:
        if map[ci][cj] != -1:
            print("returning", map[ci][cj])
            return map[ci][cj]
        else:
            cj -= 1


def hasAdjasentSymbol(i, j):
    numbers = []
    tl = getLine(i - 1, j - 1)
    tm = getLine(i - 1, j)
    tr = getLine(i - 1, j + 1)
    ml = getLine(i, j - 1)
    mr = getLine(i, j + 1)
    bl = getLine(i + 1, j - 1)
    bm = getLine(i + 1, j)
    br = getLine(i + 1, j + 1)

    if tl is not None:
        numbers.append(tl)
        if tm is not None:
            tm = None
            tr = None

    if tm is not None:
        numbers.append(tm)
        tr = None

    if tr is not None:
        numbers.append(tr)

    if ml is not None:
        numbers.append(ml)

    if mr is not None:
        numbers.append(mr)

    if bl is not None:
        numbers.append(bl)
        if bm is not None:
            bm = None
            br = None

    if bm is not None:
        numbers.append(bm)
        if br is not None:
            br = None

    if br is not None:
        numbers.append(br)

    return numbers

    # for x, y in places:
    #     if x >= len(lines):
    #         continue
    #     if y >= len(lines[x]) or x < 0 or y < 0:
    #         continue
    #     if lines[x][y] != "." and lines[x][y] != "\n":
    #         try:
    #             a = int(lines[x][y])
    #         except ValueError:
    #             return True
    # return False


def mapFrom(i, j):
    if isDone[i][j]:
        return
    if not lines[i][j].isnumeric():
        return

    ci, cj = i, j
    numbers = ""
    while True:
        if lines[ci][cj] == "\n":
            map[i][j] = int(numbers)
            return

        isDone[ci][cj] = True
        try:
            n = int(lines[ci][cj])
            numbers += str(n)
            map[ci][cj] = -1
            cj += 1
        except ValueError:
            map[i][j] = int(numbers)
            return


for i in range(len(lines)):
    isDone.append([])
    map.append([])
    for j in range(len(lines[i])):
        isDone[i].append(False)
        map[i].append(-2)

for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        symb = lines[i][j]
        mapFrom(i, j)


for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        print(str(map[i][j]).rjust(5), end="")
    print()

rats = 0
for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        if lines[i][j] == "*":
            adNumbers = hasAdjasentSymbol(i, j)
            print(adNumbers)
            if len(adNumbers) == 2:
                rats += adNumbers[0] * adNumbers[1]
print(rats)
