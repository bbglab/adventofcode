#!/bin/env python3
import itertools


def invalid_preamble_number(numbers, preamble):
    for p in range(preamble, len(numbers)):
        if not any(a + b == numbers[p] for a, b in itertools.combinations(numbers[p - preamble:p], 2)):
            yield numbers[p]


def contiguous_set_code(numbers, total):
    num_set = []
    num_set_sum = 0
    for n in numbers:
        num_set += [n]
        num_set_sum += n
        while num_set_sum > total:
            num_set_sum -= num_set.pop(0)
        if num_set_sum == total:
            return min(num_set) + max(num_set)
    return 0


def main():
    with open("input.txt") as fd:
        numbers = [int(line.strip()) for line in fd.readlines()]

    part1 = next(invalid_preamble_number(numbers, 25))
    print("Part One", part1)

    part2 = contiguous_set_code(numbers, part1)
    print("Part Two", part2)


main()
