#!/bin/env python3
from collections import Counter
from functools import lru_cache


def main():
    with open("input.txt") as fd:
        numbers = list(sorted(int(line.strip()) for line in fd.readlines()))

    adapter = numbers[-1] + 3
    part1 = Counter(b - a for a, b in zip([0] + numbers, numbers + [adapter]))
    print("Part One:", part1[1] * part1[3])

    @lru_cache
    def part_two(p=0):
        if p == len(ndiff):
            return 1
        return sum(part_two(p + i + 1) for i in range(ndiff[p]))

    ndiff = [sum([b - a <= 3, c - a <= 3, d - a <= 3]) for a, b, c, d in zip(
        [0] + numbers,
        numbers + [adapter],
        numbers[1:] + [adapter, adapter + 3],
        numbers[2:] + [adapter, adapter + 3, adapter + 6]
    )]
    part2 = part_two()
    print("Part Two:", part2)


main()
