"""
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains program ID 0:

    Program 0 by definition.
    Program 2, directly connected to program 0.
    Program 3 via program 2.
    Program 4 via program 2.
    Program 5 via programs 6, then 4, then 2.
    Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

--- Part Two ---

There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?

"""

def parse(lines):
    d = {}
    for line in lines:
        l = line.strip()
        k, v = l.split(' <-> ')
        d[k] = v.split(', ')
    return d

def read():
    with open('inputs/day12.txt') as fd:
        return fd.readlines()


test_list = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split('\n')


def find_group(direct_conections, id):
    connected = {prog for prog in direct_conections[id]}
    toexplore = connected.copy()
    explored = set()
    while toexplore:
        prog = toexplore.pop()
        if prog in explored:
            continue
        else:
            for p in direct_conections[prog]:
                toexplore.add(p)
                connected.add(p)
            explored.add(prog)
    return connected


def test1():
    assert 6 == len(find_group(parse(test_list), '0'))


def part1():
    print(len(find_group(parse(read()), '0')))


def count_groups(direct_conections):
    ungrouped_progs = list(direct_conections.keys())
    grouped = set()
    groups = 0
    while ungrouped_progs:
        prog = ungrouped_progs[0]
        grouped.update(find_group(direct_conections, prog))
        ungrouped_progs = [prog for prog in direct_conections.keys() if prog not in grouped]
        groups += 1
    return groups


def test2():
    assert 2 == count_groups(parse(test_list))


def part2():
    print(count_groups(parse(read())))


if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()
