import os
import sys
from typing import List, Tuple
from aocd import get_data, submit
import re
from dataclasses import dataclass

filename = "input.txt"

### Not really mine :( was stuck on this one and didn't have the energy
### Got it from r/xelf on reddit
### Refactored and undesrtood with chatGPT


def parse_data():
    data = {}
    for line in open(filename).read().splitlines():
        if line.startswith("seeds:"):
            yield list(map(int, re.findall("\d+", line)))
        elif line.endswith(":"):
            key = line[:-1]
        elif line.strip():
            data.setdefault(key, []).append([*map(int, line.split())])
    yield data


def part1(seeds, data, small=float("inf")):
    small = float("inf")
    for s in seeds:
        for k in data:
            s = next((s + d - o for d, o, a in data[k] if o <= s < o + a), s)
        small = s if s < small else small
    return small


def part2(seed_ranges, category_mappings):
    # Initialize the smallest location number to infinity.
    smallest_location = float("inf")

    # Iterate over pairs of seed range base and length from the seed_ranges list.
    for base_seed, range_length in zip(seed_ranges[::2], seed_ranges[1::2]):
        # Initialize the list of ranges to process with the current seed range.
        ranges_to_process = [(base_seed, base_seed + range_length)]

        # Iterate over each category (like soil, fertilizer, etc.) in the mappings.
        for category in category_mappings:
            # Create an updated list of ranges by applying the current category's mappings.
            updated_ranges = [
                new_range
                for mapping in category_mappings[
                    category
                ]  # Iterate over each mapping in the current category.
                for new_range in split_range(
                    mapping, ranges_to_process
                )  # Apply mapping and get new ranges.
            ] + ranges_to_process  # Combine new ranges with the existing ones.

            # Update the list of ranges to process with the newly formed ranges.
            ranges_to_process = updated_ranges

        # Find the smallest starting number in the current set of ranges.
        smallest_in_current_range = min(ranges_to_process)[0]

        # Update the smallest location number if the current smallest is lower.
        smallest_location = min(smallest_location, smallest_in_current_range)

    # Return the smallest location number found across all seed ranges.
    return smallest_location


def split_range(mapping, current_ranges):
    destination_start, origin_start, range_length = mapping
    new_ranges = []
    for range_start, range_end in current_ranges:
        # Calculate potential split points based on the current range and mapping
        before_split_start, before_split_end = range_start, min(range_end, origin_start)
        mapped_split_start, mapped_split_end = max(range_start, origin_start), min(
            range_end, origin_start + range_length
        )
        after_split_start, after_split_end = (
            max(origin_start + range_length, range_start),
            range_end,
        )

        # Append the range before the mapped area, if it exists
        if before_split_end > before_split_start:
            new_ranges.append((before_split_start, before_split_end))

        # Yield the mapped range, adjusted by the mapping offset
        if mapped_split_end > mapped_split_start:
            yield (
                mapped_split_start - origin_start + destination_start,
                mapped_split_end - origin_start + destination_start,
            )

        # Append the range after the mapped area, if it exists
        if after_split_end > after_split_start:
            new_ranges.append((after_split_start, after_split_end))

    current_ranges[:] = new_ranges


# print(solve_a(input[0], input[1]))
# submit(solve_a(input[0], input[1]), part="a", day=5, year=2023)
data = parse_data()
seeds, cats = next(data), next(data)
submit(part1(seeds, cats), part="a", day=5, year=2023)
submit(part2(seeds, cats), part="b", day=5, year=2023)
