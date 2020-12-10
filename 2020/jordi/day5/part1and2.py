#!/bin/env python3

def seat_id(v):
    row = int(v[:7].replace("B", "1").replace("F", "0"), 2)
    col = int(v[7:].replace("R", "1").replace("L", "0"), 2)
    return row * 8 + col


def main():
    with open('./input.txt') as fd:
        lines = fd.readlines()

    seats = set(map(seat_id, lines))
    max_seat = max(seats)
    first_empty_seat = next(filter(lambda x: x not in seats and x + 1 in seats and x - 1 in seats, range(max_seat)))

    print("Part One:", max_seat)
    print("Part Two:", first_empty_seat)


main()
