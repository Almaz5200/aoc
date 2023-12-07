import os
import math
import sys
from typing import List
from aocd import get_data, submit

# lines = get_data(day=7, year=2023)


all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "K", "Q", "A"]


def hand_weight(h):
    max_weight = 0
    J_i = []
    for i in range(5):
        if h[i] == "J":
            J_i.append(i)

    for i in range(len(all_cards) ** len(J_i)):
        h_copy = list(h)
        for j in range(len(J_i)):
            h_copy[J_i[j]] = all_cards[i % len(all_cards)]
            i = i // len(all_cards)
        max_weight = max(max_weight, hand_weight_single(h_copy))

    return max_weight


def hand_weight_single(h):
    weight = 0

    h = sorted(h)

    if h[0] == h[4]:
        return 7

    if h[0] == h[3] or h[1] == h[4]:
        return 6

    if (h[0] == h[2] and h[3] == h[4]) or (h[0] == h[1] and h[2] == h[4]):
        return 5

    if h[0] == h[2] or h[1] == h[3] or h[2] == h[4]:
        return 4

    if (
        (h[0] == h[1] and h[2] == h[3])
        or (h[0] == h[1] and h[3] == h[4])
        or (h[1] == h[2] and h[3] == h[4])
    ):
        return 3

    if h[0] == h[1] or h[1] == h[2] or h[2] == h[3] or h[3] == h[4]:
        return 2

    return 1


def card_weight(c):
    if c == "A":
        return 14
    if c == "K":
        return 13
    if c == "Q":
        return 12
    if c == "J":
        # return 11
        return 1
    if c == "T":
        return 10

    return int(c)


with open(os.path.join(sys.path[0], "input.txt")) as f:
    lines = f.read()


def parse_input(s):
    lines = s.splitlines()
    bids = [{"hand": line.split()[0], "bid": line.split()[1]} for line in lines]

    return bids


def sortingKey(x):
    key = x["weight"]
    for i in range(5):
        key = key * 100 + card_weight(x["hand"][i])
    return key


def solve_a(data):
    d = data
    for i in range(len(d)):
        d[i]["weight"] = hand_weight(d[i]["hand"])

    d.sort(key=sortingKey, reverse=True)
    d.reverse()

    total = 0
    for i in range(len(d)):
        total += (i + 1) * int(d[i]["bid"])

    return total


def solve_b(data):
    return 0


data = parse_input(lines)
print(solve_a(data))

# submit(solve_a(data), part="a", day=7, year=2023)
# submit(solve_a(data), part="b", day=7, year=2023)
