import os
import re
import hashlib
from functools import partial


class Floor:

    valid = 'bcdef'
    moves = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]

    def __init__(self, code):
        self.code = code
        self.steps = ''
        self.x = 0
        self.y = 0
        self.max_size = 4

    def get_hash(self, steps):
        string = self.code + steps
        m = hashlib.md5()
        m.update(string.encode('ascii'))
        return m.hexdigest()

    def possible_moves(self, x, y, steps):
        next_moves = []
        hash_values = self.get_hash(steps)[:4]
        for index, v in enumerate(hash_values):
            if v in Floor.valid:
                move, move_x, move_y = Floor.moves[index]
                move_x += x
                move_y += y
                if 0 <= move_x < self.max_size and 0 <= move_y < self.max_size:
                    next_moves.append((move_x, move_y, steps+move))
        return next_moves

    def shortest_path(self):
        current_level = []
        next_level = []
        while self.x != self.max_size-1 or self.y != self.max_size-1:
            for moves in self.possible_moves(self.x, self.y, self.steps):
                next_level.append(moves)
            if not current_level:
                current_level = next_level
                next_level = []
            self.x, self.y, self.steps = current_level.pop()
        return self.steps

    def recursive_search(self, found_paths, x=0,y=0, steps=''):
        if x == self.max_size-1 and y == self.max_size -1:
            found_paths.append(steps)
            return
        for values in self.possible_moves(x,y,steps):
            self.recursive_search(found_paths, *values)
        return

    def longest_path(self):
        paths = []
        self.recursive_search(paths)
        return max(map(len, paths))

    def longest_path_non_recursive(self):
        current_level = []
        next_level = []
        solutions = []
        while True:
            if self.x == self.y == self.max_size -1:
                # solution found
                solutions.append((self.x, self.y, self.steps))
            else:
                for moves in self.possible_moves(self.x, self.y, self.steps):
                    next_level.append(moves)
            if not current_level:
                if not next_level:
                    break
                current_level = next_level
                next_level = []

            self.x, self.y, self.steps = current_level.pop()
        return len(solutions[-1][2])


if __name__ == '__main__':
    floor = Floor('qzthpkfp')
    print('Part1: ', floor.shortest_path())

    floor = Floor('qzthpkfp')
    print('Part2: ', floor.longest_path_non_recursive())
