import re
import os
import numpy as np


regex = re.compile(r'\(([0-9]+)x([0-9]+)\)')

def decompress(string):
    output = ''
    prev_end = 0
    iterator = regex.finditer(string)
    for match in iterator:
        start, end = match.span()
        if start < prev_end:
            continue
        output += string[prev_end:start]
        letters, amount = match.groups()
        letters = int(letters)
        amount = int(amount)
        output += string[end:end+letters]*amount
        prev_end = end+letters
    else:
        output += string[prev_end:]
    return output

def count_letters(string):
    return len(string) - string.count(' ')

def decompress_v2(string):
    output = string
    while regex.search(output):
        print(regex.search(output))
        output = decompress(output)
    return output

## Epanding the string to count is too expensive.
# count letters in decompression
def count_decompress(string):
    whitespaces = string.count(' ')
    chars = 0
    prev_end = 0
    iterator = regex.finditer(string)
    for match in iterator:
        start, end = match.span()
        if start < prev_end:
            continue
        chars += start - prev_end
        letters, amount = match.groups()
        letters = int(letters)
        amount = int(amount)
        chars += letters*amount
        prev_end = end + letters
    else:
        chars += len(string) - prev_end
    return chars - whitespaces

def count_decompress_v2(string):
    whitespaces = string.count(' ')
    factors = [1]*len(string)
    iterator = regex.finditer(string)
    for match in iterator:
        start, end = match.span()
        letters, amount = match.groups()
        letters = int(letters)
        amount = int(amount)
        factors[start:end] = [0]*(end-start)
        factors[end:end+letters] = [i*amount for i in factors[end:end+letters]]
    chars = sum(factors)
    return chars - whitespaces

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    with open(file) as fd:
        string = fd.readline().strip()
    expanded_string = decompress(string)
    print('Part1: ', count_letters(expanded_string))
    print('Part1 version 2: ', count_decompress(string))

    # doble_decompression = decompress_v2(string)
    # print('Part 2:', count_letters(doble_decompression))
    print('Part 2:', count_decompress_v2(string))
