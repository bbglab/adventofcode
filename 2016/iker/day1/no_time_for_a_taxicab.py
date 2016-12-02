"""
Day 1: No Time for a Taxicab
"""


## PART 1

# Possible orientations
import os

orients = ['north', 'east', 'south', 'west']

# For each orientation, how to operate
operations = [(0,1), (1,0), (0,-1), (-1,0)]

def turn(orient_index, direction):
    """
    change the current orientation according to
    the new directions

    Args:
        orient_index (int): index in the orient list for the
           current orientations
        direction (str): R or L

    Returns:
        int

    """
    if direction == 'R':
        orient_index += 1
        if orient_index == 4:
            orient_index = 0
    else:
        orient_index -= 1
        if orient_index == -1:
            orient_index = 3
    return orient_index

def get_move(move):
    """
    Parses the possible moves into the direction and the amount

    E.g. R2 (2 blocks to the right), L8 (8 directions to the left)

    Args:
        move (str):

    Returns:
        tuple. Direction of the move and amount of bocks moved

    """
    return move[0], int(move[1:])

def apply_move(pos, orient_index, amount):
    """
    Change the currento position to the new one

    Args:
        pos (tuple): coordinates of current position
        orient_index (int): index in the orient list of the
          direction of the move
        amount (int): blocks to move

    Returns:
        tuple. New coordinates

    """
    x, y = pos
    x += amount * operations[orient_index][0]
    y += amount * operations[orient_index][1]
    return x, y

def move(instructions):
    """
    Move from 0,0 following the instructions

    Args:
        instructions (list): list of movements

    Returns:
        tuple. End point coordinates

    """
    pos = (0,0)
    orient_index = 0
    for move in instructions:
        direction, amount = get_move(move)
        orient_index = turn(orient_index, direction)
        pos = apply_move(pos, orient_index, amount)
    return abs(pos[0])+abs(pos[1])



## PART 2


def track_move(pos, orient_index, amount):
    """
    Get all coordinates visited in the move

    Args:
        pos (tuple): current coordinates
        orient_index (int): index of the direction in orients list
        amount (int): blocks moved

    Returns:
        list. Coordinates visited

    """
    x, y = pos
    visited = []
    for i in range(1, amount+1):
        visited.append((x + i * operations[orient_index][0], y + i * operations[orient_index][1]))
    return visited

def get_first_revisit(instructions):
    """
    Follow the instructions until you revisit a point

    Args:
        instructions (list): list of movements

    Returns:
        tuple. First position visited twice

    """
    pos = (0,0)
    orient_index = 0
    seen = [(0,0)]
    for move in instructions:
        direction, amount = get_move(move)
        orient_index = turn(orient_index, direction)
        visited = track_move(pos, orient_index, amount)
        for v in visited:
            if v in seen:
                return abs(v[0])+abs(v[1])
            else:
                seen.append(v)
        pos = seen[-1]
    return None


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    with open(file) as fd:
        input = fd.readline().strip()
    instructions = input.split(', ')
    print('Part1: ', move(instructions))

    print('Part2: ', get_first_revisit(instructions))
