"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

    Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
    Exchange, written xA/B, makes the programs at positions A and B swap places.
    Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do the following dance:

    s1, a spin of size 1: eabcd.
    x3/4, swapping the last two programs: eabdc.
    pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?


--- Part Two ---

Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

    s1, a spin of size 1: cbaed.
    x3/4, swapping the last two programs: cbade.
    pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?

"""

import string


def read():
    with open('inputs/day16.txt') as fd:
        return fd.readline().strip().split(',')


def parse(instruction):
    name = instruction[0]
    params = instruction[1:]
    if name == 's':
        params = [int(params)]
    else:
        params = params.split('/')
        if name == 'x':
            params = list(map(int, params))
    return name, params


test_instructions = [parse(inst) for inst in ['s1', 'x3/4', 'pe/b']]


class Programs:

    def __init__(self, progs):
        self.progs = progs
        self.length = len(self.progs)
        self.instructions_dict = {'s': self.spin, 'x': self.exchange, 'p': self.partner}

    def spin(self, pos):
        pos = pos % self.length
        if pos > 0:
            tmp = self.progs[-pos:]
            progs = tmp + self.progs
            self.progs = progs[:self.length]

    def exchange(self, pos1, pos2):
        v1 = self.progs[pos1]
        v2 = self.progs[pos2]
        self.progs = self.progs[:pos1] + v2 + self.progs[pos1+1:]
        self.progs = self.progs[:pos2] + v1 + self.progs[pos2+1:]

    def partner(self, prog1, prog2):
        self.exchange(self.progs.index(prog1), self.progs.index(prog2))

    def dance(self, instructions):
        for inst, params in instructions:
            self.instructions_dict[inst](*params)


def test1():
    p = Programs('abcde')
    p.dance(test_instructions)
    assert 'baedc' == p.progs


def part1():
    p = Programs(string.ascii_lowercase[:16])
    p.dance(list(map(parse, read())))
    print(p.progs)


def part2():
    initial_status = string.ascii_lowercase[:16]
    status = initial_status
    instructions = list(map(parse, read()))
    count = 0

    # Find number of iterations to go back to the initial state
    while True:
        p = Programs(status)
        p.dance(instructions)
        count += 1
        status = p.progs
        if status == initial_status:
            break

    status = initial_status
    for _ in range(10**9 % count):
        p = Programs(status)
        p.dance(instructions)
        status = p.progs
    print(status)


if __name__ == '__main__':
    # test1()
    # part1()
    part2()