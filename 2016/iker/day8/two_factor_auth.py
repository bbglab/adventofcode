import re
import os
import numpy as np


class Screen():

    rect_regex = re.compile(r'rect ([0-9]+)x([0-9]+)')
    rotate_regex = re.compile(r'rotate (row|column) (x|y)=([0-9]+) by ([0-9]+)')

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.screen = [[0]*columns for i in range(rows)]

    def rect(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                self.screen[i][j] = 1

    def rotate_row(self, index, amount):
        original = self.screen[index][:]
        for j in range(self.columns):
            self.screen[index][j] = original[j-amount]

    def rotate_column(self, index, amount):
        original = [row[index] for row in self.screen]
        for i in range(self.rows):
            self.screen[i][index] = original[i-amount]

    def proccess_instruction(self, instruction):
        m = Screen.rect_regex.match(instruction)
        if m:
            columns, rows = m.groups()
            self.rect(int(rows), int(columns))

        else:
            _, type, index, amount = Screen.rotate_regex.match(
                instruction).groups()
            if type == 'x':
                self.rotate_column(int(index), int(amount))
            else:
                self.rotate_row(int(index), int(amount))

    def pixels_on(self):
        return np.sum(self.screen)

    def apply_instructions(self, instructions):
        for ins in instructions:
            self.proccess_instruction(ins)
        return self.pixels_on()

    def show(self):
        for l in self.screen:
            print([str(8) if i else ' ' for i in l])

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    instructions = []
    with open(file) as fd:
        for line in fd:
            instructions.append(line.strip())
    screen = Screen(6,50)
    print('Part1: ', screen.apply_instructions(instructions))

    print('Part 2:', screen.show())
