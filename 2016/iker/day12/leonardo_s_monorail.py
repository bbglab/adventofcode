"""
Jordi explained that a recursive search may not work as you might
first follow an extremely long path.
Thus, the process should be done by levels
"""
import os
from collections import defaultdict


class Computer:

    def __init__(self):
        self.operations = {'cpy': self.copy, 'inc': self.add, 'dec': self.subs, 'jnz': self.jump}
        self.registers = defaultdict(int)
        self.instruction = 0

    def run(self, program):
        while self.instruction < len(program):
            values = program[self.instruction].split(' ')
            self.operations[values[0]](*(values[1:]))
            self.instruction += 1

    def get_val(self, v):
        try:
            return int(v)
        except ValueError:
            return self.registers[v]

    def copy(self, value, register):
        self.registers[register] = self.get_val(value)

    def add(self, register):
        self.registers[register] += 1

    def subs(self, register):
        self.registers[register] -= 1

    def jump(self, register, amount):
        if self.get_val(register) != 0:
            self.instruction += (int(amount) - 1)


    def get(self, register=None):
        if register is None:
            return self.registers
        else:
            return self.registers[register]



if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    program = []
    with open(file) as fd:
        for line in fd:
            program.append(line.strip())

    computer = Computer()

    computer.run(program)

    print('Part 1:', computer.get('a'))

    program = ['cpy 1 c'] + program

    computer = Computer()

    computer.run(program)

    print('Part 2:', computer.get('a'))
