"""
Jordi explained that a recursive search may not work as you might
first follow an extremely long path.
Thus, the proccess should be done by level
"""
import re
import os


class Maze:

    def __init__(self, designers_number):
        self.number = designers_number
        self.x = 1
        self.y = 1
        self.current_level = []
        self.next_level = []
        self.steps = 0
        self.visited = [(self.x, self.y)]

    def moves(self):
        return [pair for pair in [(self.x, self.y+1), (self.x, self.y-1),
                                  (self.x+1, self.y), (self.x-1, self.y)]]

    def is_valid(self, coordinates):
        x, y = coordinates
        if x < 0 or y < 0:
            return False
        sum = (x*x + 3*x + 2*x*y + y + y*y) + self.number
        if bin(sum).count('1') % 2 == 0:
            return True
        else:
            return False

    def is_new(self, coordinates):
        return not coordinates in self.visited

    def reach(self, coordinates):
        dest_x, dest_y = coordinates
        while self.x != dest_x or self.y != dest_y:
            for next_coordinates in self.moves():
                if self.is_new(next_coordinates) and \
                        self.is_valid(next_coordinates):
                    self.next_level.append(next_coordinates)
                    self.visited.append(next_coordinates)
            if not self.current_level:
                self.current_level = self.next_level
                self.next_level = []
                self.steps += 1
            self.x, self.y = self.current_level.pop()
        return self.steps

    def make_steps(self, steps):
        while self.steps < steps:
            for next_coordinates in self.moves():
                if self.is_new(next_coordinates) and \
                        self.is_valid(next_coordinates):
                    self.next_level.append(next_coordinates)
                    self.visited.append(next_coordinates)
            if not self.current_level:
                self.current_level = self.next_level
                self.next_level = []
                self.steps += 1
            self.x, self.y = self.current_level.pop()
        return len(self.visited)




if __name__ == '__main__':
    maze = Maze(1364)

    print('Part 1:', maze.reach((31,39)))

    maze = Maze(1364)

    print('Part 2:', maze.make_steps(50))