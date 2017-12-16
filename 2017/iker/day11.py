"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

"""
from collections import Counter, defaultdict

def read():
    with open('inputs/day11.txt') as fd:
        return fd.read().strip().split(',')


oppossites = {'n': 's', 'ne': 'sw', 'nw': 'se'}
oppossites.update({v: k for k,v in oppossites.items()})


def reduce(moves):
    counts = Counter(moves)
    reduced = defaultdict(int)
    for k, v in oppossites.items():
        value = counts[k] - counts[v]
        if value > 0:
            reduced[k] = value
    return reduced


coords = {'n': (0,2), 'ne': (1,1), 'nw': (-1, 1)}
coords.update({oppossites[k]: (-v[0], -v[1]) for k, v in coords.items()})


def coordinates(items):
    x, y = 0, 0
    for k,v in items.items():
        a, b = coords[k]
        a, b = a*v, b*v
        x += a
        y += b
    return x, y


def distance(moves):
    reduced = reduce(moves)  # get only the moves that have not been compensated
    if len(reduced) == 0:
        return 0
    elif len(reduced) == 1:
        return sum(reduced.values())
    elif len(reduced) > 3:
        raise ValueError
    else:
        x, y = coordinates(reduced)
        # to move in X require 1 move
        # as moving in X also implies en move in Y we need only to move the remaining values
        return abs(x) + (abs(y) - min(abs(x), abs(y))) // 2


def test1():
    assert 3 == distance(['ne']*3)
    assert 0 == distance(['ne', 'ne', 'sw', 'sw'])
    assert 2 == distance(['ne', 'ne', 's', 's'])
    assert 3 == distance('se,sw,se,sw,sw'.split((',')))


def part1():
    print(distance(read()))


def max_distance(moves):
    max_ = 0
    for i in range(len(moves)):
        d = distance(moves[:i])
        if d > max_:
            max_ = d
    return max_


def part2():
    print(max_distance(read()))


if __name__ == '__main__':
    test1()
    part1()
    part2()
