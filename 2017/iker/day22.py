"""
--- Day 22: Sporifica Virus ---

Diagnostics indicate that the local grid computing cluster has been contaminated with the Sporifica Virus. The grid computing cluster is a seemingly-infinite two-dimensional grid of compute nodes. Each node is either clean or infected by the virus.

To prevent overloading the nodes (which would render them useless to the virus) or detection by system administrators, exactly one virus carrier moves through the network, infecting or cleaning nodes as it moves. The virus carrier is always located on a single node in the network (the current node) and keeps track of the direction it is facing.

To avoid detection, the virus carrier works in bursts; in each burst, it wakes up, does some work, and goes back to sleep. The following steps are all executed in order one time each burst:

    If the current node is infected, it turns to its right. Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)
    If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
    The virus carrier moves forward one node in the direction it is facing.

Diagnostics have also provided a map of the node infection status (your puzzle input). Clean nodes are shown as .; infected nodes are shown as #. This map only shows the center of the grid; there are many more nodes beyond those shown, but none of them are currently infected.

The virus carrier begins in the middle of the map facing up.

For example, suppose you are given a map like this:

..#
#..
...

Then, the middle of the infinite grid looks like this, with the virus carrier's position marked with [ ]:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on a clean node, so it turns left, infects the node, and moves left:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]# . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on an infected node, so it turns right, cleans the node, and moves up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Four times in a row, the virus carrier finds a clean, infects it, turns left, and moves forward, ending in the same place and still facing up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . #[#]. # . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Now on the same node as before, it sees an infection, which causes it to turn right, clean the node, and move forward:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . # .[.]# . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

After the above actions, a total of 7 bursts of activity had taken place. Of them, 5 bursts of activity caused an infection.

After a total of 70, the grid looks like this, with the virus carrier facing up:

. . . . . # # . .
. . . . # . . # .
. . . # . . . . #
. . # . #[.]. . #
. . # . # . . # .
. . . . . # # . .
. . . . . . . . .
. . . . . . . . .

By this time, 41 bursts of activity caused an infection (though most of those nodes have since been cleaned).

After a total of 10000 bursts of activity, 5587 bursts will have caused an infection.

Given your actual map, after 10000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)


--- Part Two ---

As you go to remove the virus from the infected nodes, it evolves to resist your attempt.

Now, before it infects a clean node, it will weaken it to disable your defenses. If it encounters an infected node, it will instead flag the node to be cleaned in the future. So:

    Clean nodes become weakened.
    Weakened nodes become infected.
    Infected nodes become flagged.
    Flagged nodes become clean.

Every node is always in exactly one of the above states.

The virus carrier still functions in a similar way, but now uses the following logic during its bursts of action:

    Decide which way to turn based on the current node:
        If it is clean, it turns left.
        If it is weakened, it does not turn, and will continue moving in the same direction.
        If it is infected, it turns right.
        If it is flagged, it reverses direction, and will go back the way it came.
    Modify the state of the current node, as described above.
    The virus carrier moves forward one node in the direction it is facing.

Start with the same map (still using . for clean and # for infected) and still with the virus carrier starting in the middle and facing up.

Using the same initial state as the previous example, and drawing weakened as W and flagged as F, the middle of the infinite grid looks like this, with the virus carrier's position again marked with [ ]:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

This is the same as before, since no initial nodes are weakened or flagged. The virus carrier is on a clean node, so it still turns left, instead weakens the node, and moves left:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on an infected node, so it still turns right, instead flags the node, and moves up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . F W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

This process repeats three more times, ending on the previously-flagged node and facing right:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. . W[F]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Finding a flagged node, it reverses direction and cleans the node:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. .[W]. W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The weakened node becomes infected, and it continues in the same direction:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
.[.]# . W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Of the first 100 bursts, 26 will result in infection. Unfortunately, another feature of this evolved virus is speed; of the first 10000000 bursts, 2511944 will result in infection.

Given your actual map, after 10000000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)

"""

directions = 'nesw'


directions2move = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}


test_input = """..#
#..
...""".splitlines()


def read():
    with open('inputs/day22.txt') as fd:
        return fd.read().splitlines()


def parse(lines):
    nodes = []
    size = len(lines[0].strip())
    v = size // 2
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c == '#':
                nodes.append((j-v, (i-v)*(-1)))
    return set(nodes)


def burst(infected_nodes, pos, direction):
    x, y = pos

    # next direction
    if pos in infected_nodes:
        i = (directions.index(direction) + 1) % 4

        infected_nodes.remove(pos)

    else:
        i = (directions.index(direction) - 1) % 4

        infected_nodes.add(pos)

    next_direction = directions[i]

    # next position
    a, b = directions2move[next_direction]
    next_pos = (x+a, y+b)

    return infected_nodes, next_pos, next_direction


def count_infections(initial_status, iterations):
    count = 0
    status = initial_status
    pos = (0,0)
    direction = 'n'
    for _ in range(iterations):
        prev_size = len(status)
        status, pos, direction = burst(status, pos, direction)
        count += 1 if len(status) > prev_size else 0 # should be 0 or 1
    return count


def test1():
    assert 5587 == count_infections(parse(test_input), 10**4)


def part1():
    print(count_infections(parse(read()), 10**4))


def burst2(weakened, infected, flagged, pos, direction):
    nodes_weakened, nodes_infected, nodes_flagged = weakened, infected, flagged

    x, y = pos

    # next direction
    if pos in nodes_weakened:
        i = directions.index(direction)

        nodes_weakened.remove(pos)
        nodes_infected.add(pos)

    elif pos in nodes_infected:
        i = (directions.index(direction) + 1) % 4

        nodes_infected.remove(pos)
        nodes_flagged.add(pos)

    elif pos in nodes_flagged:
        i = (directions.index(direction) + 2) % 4

        nodes_flagged.remove(pos)
    else:
        i = (directions.index(direction) - 1) % 4

        nodes_weakened.add(pos)

    next_direction = directions[i]

    # next position
    a, b = directions2move[next_direction]
    next_pos = (x+a, y+b)

    return nodes_weakened, nodes_infected, nodes_flagged, next_pos, next_direction


def count_infections2(initial_status, iterations):
    count = 0
    infected = initial_status
    weakened = set()
    flagged = set()
    pos = (0,0)
    direction = 'n'
    for _ in range(iterations):
        prev_size = len(infected)
        weakened, infected, flagged, pos, direction = burst2(weakened, infected, flagged, pos, direction)
        count += 1 if len(infected) > prev_size else 0 # should be 0 or 1
    return count


def test2():
    assert 26 == count_infections2(parse(test_input), 10**2)
    assert 2511944 == count_infections2(parse(test_input), 10**7)


def part2():
    print(count_infections2(parse(read()), 10**7))


if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()
