import numpy as np
from functools import reduce


def rotation_matrix(a):
    r = np.deg2rad(a)
    return np.array(((np.cos(r), -np.sin(r)), (np.sin(r), np.cos(r))))


INSTRUCTION_SET_ONE = {
    "F": lambda t: lambda a: (a[0] + t * a[1], a[1]),
    "N": lambda t: lambda a: (a[0] + t * np.array((0.0, 1.0)), a[1]),
    "S": lambda t: lambda a: (a[0] + t * np.array((0.0, -1.0)), a[1]),
    "E": lambda t: lambda a: (a[0] + t * np.array((1.0, 0.0)), a[1]),
    "W": lambda t: lambda a: (a[0] + t * np.array((-1.0, 0.0)), a[1]),
    "L": lambda g: lambda a: (a[0], np.matmul(a[1], rotation_matrix(-g))),
    "R": lambda g: lambda a: (a[0], np.matmul(a[1], rotation_matrix(g)))
}

INSTRUCTION_SET_TWO = {
    "F": lambda t: lambda a: (a[0] + t * a[1], a[1]),
    "N": lambda t: lambda a: (a[0], a[1] + t * np.array((0.0, 1.0))),
    "S": lambda t: lambda a: (a[0], a[1] + t * np.array((0.0, -1.0))),
    "E": lambda t: lambda a: (a[0], a[1] + t * np.array((1.0, 0.0))),
    "W": lambda t: lambda a: (a[0], a[1] + t * np.array((-1.0, 0.0))),
    "L": lambda g: lambda a: (a[0], np.matmul(a[1], rotation_matrix(-g))),
    "R": lambda g: lambda a: (a[0], np.matmul(a[1], rotation_matrix(g)))
}


def execute(instructions_set, lines, init):
    position, direction = reduce(
        lambda a, b: b(a),
        (instructions_set[line[0]](float(line[1:])) for line in lines),
        init
    )
    return np.abs(np.round(position).astype(int)).sum()


def main():
    with open("input.txt") as fd:
        lines = [line.strip() for line in fd.readlines()]

    part1 = execute(INSTRUCTION_SET_ONE, lines, (np.array((0.0, 0.0)), np.array((1.0, 0.0))))
    print("Part One:", part1)

    part2 = execute(INSTRUCTION_SET_TWO, lines, (np.array((0.0, 0.0)), np.array((10.0, 1.0))))
    print("Part Two:", part2)


main()
