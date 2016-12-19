import os
import re
import hashlib
from functools import partial


class Disc:

    def __init__(self, id, size, intitial_position, delay=1,
                 angular_velocity=1):
        self.id = int(id)
        self.size = int(size)
        self.initial_position = int(intitial_position)
        self.delay = self.id
        self.angular_velocity = angular_velocity

    def get_position(self, time):
        return (self.angular_velocity*time + self.initial_position) % self.size

    def get_position_with_delay(self, time):
        return (self.angular_velocity * (time + self.delay) +
                self.initial_position) % self.size

    def min_time_to_0(self):
        return self.size - (self.angular_velocity * self.delay + self.initial_position) % self.size


class Sculpture:

    regex = re.compile(r'Disc #([0-9]+) has ([0-9]+) positions; at time=0, '
                       r'it is at position ([0-9]+).')

    def __init__(self, description):
        self.discs = []
        for line in description:
            match = Sculpture.regex.match(line)
            if match:
                self.discs.append(Disc(*match.groups()))

        self.sort_discs()

    def sort_discs(self):
        self.discs = sorted(self.discs, key=lambda disc: disc.size)

    def solve(self):
        sol = None
        index = 0
        while sol is None:
            time = self.discs[-1].min_time_to_0() + index * self.discs[-1].size

            for disc in self.discs:
                if disc.get_position_with_delay(time) != 0:
                    break
            else:
                return time

            index += 1



if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    instructions = []
    with open(file) as fd:
        for line in fd:
            instructions.append(line.strip())

    sculpture = Sculpture(instructions)
    print('Part1: ', sculpture.solve())

    instructions.append('Disc #7 has 11 positions; at time=0, it is at position 0.')
    sculpture = Sculpture(instructions)
    print('Part 2:', sculpture.solve())
