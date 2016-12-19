import os
import re
import hashlib
from functools import partial

def generate_data(data):
    a = data
    b = reversed(data)
    b = ''.join(['1' if s == '0' else '0' for s in b])
    return a+'0'+b

regex = re.compile(r'..')

def get_checksum(data):
    checksum = ''
    for pair in regex.finditer(data):
        char1, char2 = pair.group()
        if char1 == char2:
            checksum += '1'
        else:
            checksum += '0'
    # while len(checksum) % 2 == 0:
    if len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)
    return checksum


def fill_disk(size, initial_state):
    data = initial_state
    while len(data) < size:
        data = generate_data(data)
    return data[:size], get_checksum(data[:size])


if __name__ == '__main__':
    size = 272
    init_state = '10011111011011001'
    _, checksum = fill_disk(size, init_state)
    print('Part1: ', checksum)

    size = 35651584
    _, checksum = fill_disk(size, init_state)
    print('Part2: ', checksum)
