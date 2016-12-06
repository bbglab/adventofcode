import os
from collections import Counter


def get_message(messages):
    letters = zip(*messages)
    message = ''
    for l in letters:
        message += Counter(l).most_common(1)[0][0]
    return message

def get_message2(messages):
    letters = zip(*messages)
    message = ''
    for l in letters:
        message += Counter(l).most_common()[-1][0]
    return message

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    messages = []
    with open(file) as fd:
        for line in fd:
            messages.append(line.strip())
    print('Part1: ', get_message(messages))

    print('Part 2:', get_message2(messages))
