import os

import re
import string
from collections import Counter

regex = re.compile(r'([a-z\-]*)\-([0-9]*)\[([a-z]*)\]')


def compute_checksum(room_name):
    counts = Counter(room_name).most_common()
    # The most common function does not return values in alphabetic order
    chars_by_counts = ['']*(counts[0][1]+1)
    for char, v in counts:
        if v >= counts[4][1]:
            chars_by_counts[v] += char
        else:
            # counts should be shorted by quantity
            break
    expected_checksum = []
    for chars in reversed(chars_by_counts):
        expected_checksum += sorted(chars)
    return ''.join(expected_checksum[:5])

def sum_valid_sectors(rooms):
    sum_sectors = 0
    for room in rooms:
        name, sector, checksum = regex.match(room).groups()
        expected_checksum = compute_checksum(name.replace('-', ''))
        if expected_checksum == checksum:
            sum_sectors += int(sector)
    return sum_sectors

alphabet = string.ascii_lowercase

def shift_cipher(letter, amount):
    amount = amount%len(alphabet)
    pos = alphabet.index(letter)
    pos = pos+amount
    if pos >= len(alphabet):
        pos = pos - len(alphabet)
    return alphabet[pos]


def process_name(name, number):
    processed_name = ''
    for letter in name:
        if letter == '-':
            processed_name += ' '
        else:
            processed_name += shift_cipher(letter, number)
    return processed_name

def get_room_names(rooms):
    for room in rooms:
        name, sector, checksum = regex.match(room).groups()
        expected_checksum = compute_checksum(name.replace('-', ''))
        if expected_checksum == checksum:
            name =  process_name(name, int(sector))
            if 'northpole' in name:
                print(sector,name)



if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    rooms = []
    with open(file) as fd:
        for line in fd:
            rooms.append(line.strip())
    print('Part1: ', sum_valid_sectors(rooms))

    print('Part 2:', get_room_names(rooms))
