import os
import sys
from typing import List
from aocd import get_data, submit

lines = get_data(day=4, year=2023)

pointsWon = 0


def parse_input(s):
    for line in s.splitlines():
        a, b = line.split(": ")
        left, right = b.split(" | ")
        left = set(map(int, left.split()))
        right = set(map(int, right.split()))

        assert a.startswith("Card ")
        a = int(a.split()[1])

        yield a, left, right


data = list(parse_input(lines))
copies = [1] * len(data)

for num, winning, have in data:
    num -= 1
    multiplier = copies[num]
    n = len(winning & have)
    for off in range(1, n + 1):
        off = num + off
        if off >= len(data):
            continue
        copies[off] += multiplier


print(sum(copies))
submit(sum(copies), part="b", day=4, year=2023)
