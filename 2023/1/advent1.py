import os
import sys
from typing import List

with open("input.txt") as f:
    lines = f.readlines()

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum = 0
for line in lines:
    first = -1
    last = 0
    ogLine = line

    # print(line)
    # for text, number in numbers.items():
    #     ind = ogLine.find(text)
    #     if ind != -1:
    #         line = line[:ind] + str(number) + line[ind:]
    # print(line)
    #
    # for char in line:
    #     try:
    #         num = int(char)
    #     except ValueError:
    #         continue
    #
    #     if first == -1:
    #         first = num
    #     last = num
    # sum += 10 * first + last
    digits: List[int] = []
    length = len(line)
    for i in range(length):
        try:
            num = int(line[i])
            digits.append(num)
        except ValueError:
            for text, number in numbers.items():
                if line[i : i + len(text)] == text:
                    digits.append(number)
    sum += 10 * digits[0] + digits[-1]

print(sum)
