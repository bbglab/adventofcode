"""
--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

    If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
    Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.

When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.

Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

.#.
..#
###

The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...

Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?


--- Part Two ---

How many pixels stay on after 18 iterations?

"""

init_pattern = """.#.
..#
###""".splitlines()


test_rules = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""".splitlines()


def read():
    rules = []
    with open('inputs/day21.txt') as fd:
        for line in fd:
            rules.append(line.strip())
    return rules


def parse(rules):
    r = {}
    for rule in rules:
        from_, to = rule.split(' => ')
        r[from_] = to
    return r


def rotate(pattern):
    """Rotate clockwise"""
    pattern_ = pattern.split('/')
    length = len(pattern_)
    new_pattern = [None] * length
    if length == 2:
        new_pattern[0] = pattern_[1][0] + pattern_[0][0]
        new_pattern[1] = pattern_[1][1] + pattern_[0][1]
    else:
        new_pattern[0] = pattern_[2][0] + pattern_[1][0] + pattern_[0][0]
        new_pattern[1] = pattern_[2][1] + pattern_[1][1] + pattern_[0][1]
        new_pattern[2] = pattern_[2][2] + pattern_[1][2] + pattern_[0][2]
    return '/'.join(new_pattern)


def vflip(pattern):
    pattern_ = pattern.split('/')
    length = len(pattern_)
    new_pattern = [None] * length
    if length == 2:
        new_pattern[0] = pattern_[0][1] + pattern_[0][0]
        new_pattern[1] = pattern_[1][1] + pattern_[1][0]
    else:
        new_pattern[0] = pattern_[0][2] + pattern_[0][1] + pattern_[0][0]
        new_pattern[1] = pattern_[1][2] + pattern_[1][1] + pattern_[1][0]
        new_pattern[2] = pattern_[2][2] + pattern_[2][1] + pattern_[2][0]
    return '/'.join(new_pattern)


def hflip(pattern):
    pattern_ = pattern.split('/')
    length = len(pattern_)
    new_pattern = [None] * length
    if length == 2:
        new_pattern[0] = pattern_[1]
        new_pattern[1] = pattern_[0]
    else:
        new_pattern[0] = pattern_[2]
        new_pattern[1] = pattern_[1]
        new_pattern[2] = pattern_[0]
    return '/'.join(new_pattern)


def enhance(pattern, rules):
    if pattern in rules:
        altered = rules[pattern]
    elif vflip(pattern) in rules:
        altered = rules[vflip(pattern)]
    elif hflip(pattern) in rules:
        altered = rules[hflip(pattern)]
    else:
        for k in range(3):
            pattern = rotate(pattern)
            if pattern in rules:
                altered = rules[pattern]
                break
            elif vflip(pattern) in rules:
                altered = rules[vflip(pattern)]
                break
            elif hflip(pattern) in rules:
                altered = rules[hflip(pattern)]
                break
        else:
            assert False
    return altered


def operate(state, rules):
    length = len(state)

    if len(state) % 2 == 0:
        split_size = 2
    else:
        split_size = 3

    line = 0
    size = length // split_size
    output = [''] * (split_size+1) * size
    for i in range(0, length, split_size):
        for j in range(0, length, split_size):
            pattern_items = []
            for k in range(split_size):
                pattern_items.append(state[i+k][j:j+split_size])
            pattern = '/'.join(pattern_items)
            altered = enhance(pattern, rules)
            for k, v in enumerate(altered.split('/')):
                output[line+k] += v
        line += (split_size+1)
    return output


def count_pixels_on(pattern):
    count = 0
    for line in pattern:
        count += line.count('#')
    return count


def test1():
    pattern = init_pattern
    for _ in range(2):
        pattern = operate(pattern, parse(test_rules))
    assert 12 == count_pixels_on(pattern)


def part1():
    pattern = init_pattern
    for _ in range(5):
        pattern = operate(pattern, parse(read()))
    print(count_pixels_on(pattern))


def part2():
    pattern = init_pattern
    for _ in range(18):
        pattern = operate(pattern, parse(read()))
    print(count_pixels_on(pattern))

if __name__ == '__main__':
    # test1()
    # part1()
    part2()
