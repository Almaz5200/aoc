import os
import sys
from typing import List

with open("input.txt") as f:
    lines = f.readlines()

ids = 0
sum = 0
for line in lines:
    sep1 = line.split(":")
    gameId = int(sep1[0][5:])

    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    shows = sep1[1].split(";")
    for show in shows:
        for element in show.split(","):
            element = element.strip(" ")
            sep2 = element.split(" ")
            num, color = int(sep2[0]), sep2[1].strip()
            if color == "green":
                maxGreen = max(maxGreen, num)
            if color == "blue":
                maxBlue = max(maxBlue, num)
            if color == "red":
                maxRed = max(maxRed, num)

    print("==")
    print(maxBlue)
    print(maxRed)
    print(maxGreen)
    power = maxGreen * maxRed * maxBlue
    sum += power
    if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
        ids += gameId

print(ids)
print(sum)
