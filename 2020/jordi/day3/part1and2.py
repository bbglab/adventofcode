#!/bin/env python3
from functools import reduce


def get_position(data, x, y):
    if y >= len(data) or x <= 0 or y <= 0:
        raise ValueError("Outside the map")
    line = data[y]
    xm = x % len(line)
    return line[xm]


def count_trees(data, slope):
    trees = 0
    x, y = 0, 0
    try:
        while True:
            x += slope[0]
            y += slope[1]
            m = get_position(data, x, y)
            trees += int(m == "#")
    except ValueError:
        pass
    return trees


def main():
    with open("input.txt") as fd:
        data = [line.strip() for line in fd.readlines()]

    part1 = count_trees(data, (3, 1))
    print("Part One:", part1)

    part2 = reduce(lambda a, b: a * b, map(lambda s: count_trees(data, s), ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))), 1)
    print("Part Two:", part2)


main()
