"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

"""

import collections
import operator
import re


def read():
    with open('inputs/day8.txt') as fd:
        for line in fd:
            yield line.strip()



test_instructions = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')


comparisons = {'>': operator.gt, '>=': operator.ge, '<': operator.lt,
               '<=': operator.le, '==': operator.eq, '!=': operator.ne}


regex = re.compile(r'(?P<register>\w+?) (?P<operation>inc|dec) (?P<amount>-?[0-9]+) if (?P<reg>\w+?) (?P<operator>.+?) (?P<value>-?[0-9]+)')


def parse(instruction):
    match = regex.search(instruction)
    register = match.group('register')
    operation = operator.add if match.group('operation') == 'inc' else operator.sub
    value = int(match.group('amount'))
    condition_reg = match.group('reg')
    condition_operation = comparisons[match.group('operator')]
    condition_value = int(match.group('value'))
    return register, operation, value, (condition_reg, condition_operation, condition_value)


registers = collections.defaultdict(int)


def process(instruction):
    reg, operation, val, condition = parse(instruction)
    cond_reg, cond_op, cond_val = condition
    if cond_op(registers[cond_reg], cond_val):
        registers[reg] = operation(registers[reg], val)


def maximum(instructions):
    for inst in instructions:
        process(inst)
    return max(registers.values())


def test1():
    assert 1 == maximum(test_instructions)


def part1():
    print(maximum(read()))


def maximum_held(instructions):
    max_ = 0
    for inst in instructions:
        process(inst)
        curr_max = max(registers.values())
        if curr_max > max_:
            max_ = curr_max
    return max_


def test2():
    assert 10 == maximum_held(test_instructions)


def part2():
    print(maximum_held(read()))


if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()
