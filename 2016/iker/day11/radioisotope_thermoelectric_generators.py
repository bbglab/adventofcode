"""
Jordi explained that a recursive search may not work as you might
first follow an extremely long path.
Thus, the process should be done by levels
"""
import re
import os
import numpy as np


class Microchip:
    def __init__(self, material):
        self.material = material

    def is_compatible(self, material):
        return material == self.material


class Generator:
    def __init__(self, material):
        self.material = material

    def is_compatible(self, material):
        return material == self.material


class Building:
    generator_regex = re.compile(r'(?P<material>\b\w+\b) generator')
    microchip_regex = re.compile(r'(?P<material>\b\w+)-compatible microchip')

    def __init__(self, instructions):
        self.floors = [[] for i in range(len(instructions))]
        self.elevator = 0
        self.visited = []
        for index, instruction in enumerate(instructions):
            for match in Building.generator_regex.finditer(instruction):
                self.floors[index].append(Generator(match.groups()))
            for match in Building.microchip_regex.finditer(instruction):
                self.floors[index].append(Microchip(match.groups()))
        self.add_status()

        # Search levels
        self.current_level = []
        self.next_level = []
        self.level_index = 0

    def add_status(self, building_distribution=None):
        self.visited.append(self.get_status(building_distribution))

    def get_status(self, building_distribution=None):
        state = []

        if building_distribution is None:
            floors = self.floors
            elevator = self.elevator
        else:
            elevator, floors = building_distribution

        for floor in floors:
            microchips = 0
            generators = 0
            for item in floor:
                if isinstance(item, Microchip):
                    microchips += 1
                else:
                    generators += 1
            state.append((elevator, microchips, generators))
        return state

    def has_finished(self):
        for floor in self.floors[:-1]:
            if len(floor) > 0:
                return False
        return True

    def copy_floors(self, floors=None):
        if floors is None:
            floors = self.floors
        copied = []
        for floor in floors:
            copied.append(floor[:])
        return copied

    def is_new(self, building_distribution):
        status = self.get_status(building_distribution)
        return not status in self.visited


    def solve(self):
        while not self.has_finished():
            # add all possible moves from current level

            for i in range(len(self.floors[self.elevator])):  # Loop through current floor items
                for move_to in (self.elevator - 1, self.elevator + 1):  # Possible moves are one floor up or down
                    if 0 <= move_to < len(self.floors):  # Check if the move is in range

                        # Move one item
                        new_floors = self.copy_floors()
                        item = new_floors[self.elevator].pop(i)
                        new_floors[move_to].append(item)
                        if self.is_new((move_to,new_floors)) and \
                                self.is_valid_floor(new_floors[self.elevator]) and \
                                self.is_valid_floor(new_floors[move_to]):
                            self.next_level.append((move_to, new_floors))
                            self.add_status((move_to, new_floors))

                        # Move 2 items
                        for j in range(i, len(new_floors[self.elevator])):
                            # We start at i because we have already taken 1 element
                            new_floors_2 = self.copy_floors(new_floors)
                            item = new_floors_2[self.elevator].pop(j)
                            new_floors_2[move_to].append(item)
                            if self.is_new((move_to, new_floors_2)) and \
                                    self.is_valid_floor(new_floors_2[self.elevator]) and \
                                    self.is_valid_floor(new_floors_2[move_to]):
                                self.next_level.append((move_to, new_floors_2))
                                self.add_status((move_to,new_floors_2))

            if not self.current_level:
                # If we have visited all possible configurations in the current level, move to the next
                self.current_level = self.next_level
                self.next_level = []
                self.level_index += 1
            self.elevator, self.floors = self.current_level.pop(0)
        return self.level_index




    def is_valid_floor(self, floor):
        microchips = [chip for chip in floor if isinstance(chip, Microchip)]
        generators = [generator for generator in floor if isinstance(generator, Generator)]

        if len(generators) == 0:
            return True
        for microchip in microchips:
            for generator in generators:
                if generator.is_compatible(microchip.material):
                    break
            else:
                return False
        return True


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    instructions = []
    with open(file) as fd:
        for line in fd:
            instructions.append(line.strip())

    building = Building(instructions)

    print('Part 1:', building.solve())

    instructions[0] = instructions[0] + 'You also find and elerium generator, an elerium-compatible microchip' +\
        'a dilithium generator and a dilithium-compatible microchip.'

    building = Building(instructions)

    print('Part 2:', building.solve())
