#!/bin/env python3
from collections import namedtuple
from itertools import cycle

Position = namedtuple("Position", ["row", "col"])


def is_seat(s):
    return s == '#' or s == 'L'


def is_occupied(s):
    return s == '#'


def adjacent_seats(seats, p: Position):
    res = []
    for r, c in [(p.row, p.col - 1), (p.row, p.col + 1), (p.row + 1, p.col), (p.row - 1, p.col), (p.row - 1, p.col - 1), (p.row - 1, p.col + 1), (p.row + 1, p.col - 1), (p.row + 1, p.col + 1)]:
        try:
            if r < 0 or c < 0:
                continue
            res += [seats[r][c]]
        except IndexError:
            pass
    return res


def first_seen(seats, pos: Position):

    res = []
    rleft = range(pos.col - 1, -1, -1)
    rright = range(pos.col + 1, len(seats[0]))
    rup = range(pos.row - 1, -1, -1)
    rdown = range(pos.row + 1, len(seats))
    for rrow, rcol in [(cycle([pos.row]), rleft), (cycle([pos.row]), rright), (rup, cycle([pos.col])), (rdown, cycle([pos.col])), (rup, rleft), (rdown, rleft), (rup, rright), (rdown, rright)]:
        try:
            res += [next(filter(is_seat, (seats[r][c] for r, c in zip(rrow, rcol))))]
        except StopIteration:
            pass

    return res


def next_seat_state(seats, pos: Position, selection_method=adjacent_seats, tolerance=4):
    s = seats[pos.row][pos.col]
    occupied = sum(1 for _ in filter(is_occupied, (s for s in selection_method(seats, pos))))
    if s == 'L' and occupied == 0:
        return '#'
    if s == '#' and occupied >= tolerance:
        return 'L'
    return s


def next_seats_state(seats, selection_method=adjacent_seats, tolerance=4):
    new_seats = []
    for r in range(len(seats)):
        line = []
        for c in range(len(seats[0])):
            line.append(next_seat_state(seats, Position(r, c), selection_method=selection_method, tolerance=tolerance))
        new_seats.append(line)
    return new_seats


def occupied_at_equilibrium(seats, selection_method=adjacent_seats, tolerance=4):
    nseats = next_seats_state(seats, selection_method=selection_method, tolerance=tolerance)
    while seats != nseats:
        seats = nseats
        nseats = next_seats_state(seats, selection_method=selection_method, tolerance=tolerance)

    return sum(sum(1 for _ in filter(is_occupied, row)) for row in seats)


def main():
    with open("sample.txt") as fd:
        seats = [[s for s in line.strip()] for line in fd.readlines()]

    part1 = occupied_at_equilibrium(seats)
    print("Part One:", part1)

    part2 = occupied_at_equilibrium(seats, selection_method=first_seen, tolerance=5)
    print("Part Two:", part2)


main()
