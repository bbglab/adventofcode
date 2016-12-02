"""
Bathroom Security
"""
import os

"""
Keypad
123
456
789
"""

pad = {
    1: {'U': 1, 'D':4, 'L': 1, 'R': 2},
    2: {'U': 2, 'D':5, 'L': 1, 'R': 3},
    3: {'U': 2, 'D':6, 'L': 2, 'R': 3},
    4: {'U': 1, 'D':7, 'L': 4, 'R': 5},
    5: {'U': 2, 'D':8, 'L': 4, 'R': 6},
    6: {'U': 3, 'D':9, 'L': 5, 'R': 6},
    7: {'U': 4, 'D':7, 'L': 7, 'R': 8},
    8: {'U': 5, 'D':8, 'L': 7, 'R': 9},
    9: {'U': 6, 'D':9, 'L': 8, 'R': 9}
}


def get_code(instructions):
    button = 5
    code = 0
    for instructions_line in instructions:
        for move in instructions_line:
            button = pad[button][move]
        code = code *10 + button
    return code

"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

pad2 = {
    '1': {'D': '3'},
    '2': {'R': '3', 'D': '6'},
    '3': {'U':'1', 'D':'7', 'L':'2', 'R': '4'},
    '4': {'D':'8', 'L':'3'},
    '5': {'R': '6'},
    '6': {'U':'2', 'D':'A', 'L':'5', 'R': '7'},
    '7': {'U':'3', 'D':'B', 'L':'6', 'R': '8'},
    '8': {'U':'4', 'D':'C', 'L':'7', 'R': '9'},
    '9': {'L':'8'},
    'A': {'U':'6','R': 'B'},
    'B': {'U':'7', 'D':'D', 'L':'A', 'R': 'C'},
    'C': {'U':'8', 'L':'B'},
    'D': {'U': 'B'}
}

def get_code2(instructions):
    button = '5'
    code = ''
    for instructions_line in instructions:
        for move in instructions_line:
            button = pad2[button].get(move, button)
        code += button
    return code

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    instructions = []
    with open(file) as fd:
        for line in fd:
            instructions.append(line.strip())
    print('Part1: ', get_code(instructions))
    print('Part2: ', get_code2(instructions))