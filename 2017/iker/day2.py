"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

    In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    In the second row, the two numbers are 9 and 3; the result is 3.
    In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

"""

def read():
    with open('inputs/day2.txt') as fd:
        return fd.read()


def parse(spreadsheet_txt):
    rows = spreadsheet_txt.split('\n')
    spreadsheet = []
    for r in rows:
        spreadsheet.append(list(map(int, r.strip().split())))
    return spreadsheet


def checksum(spreadsheet):
    checksum_ = 0
    for row in spreadsheet:
        checksum_ += max(row) - min(row)
    return checksum_

def test1():
    spreadsheet = """5 1 9 5
                7 5 3
                2 4 6 8"""
    assert 18 == checksum(parse(spreadsheet))

def part1():
    print(checksum(parse(read())))


def dividers_sum(spreadsheet):
    sum_ = 0
    for row in spreadsheet:
        found = False
        for i, x in enumerate(row[:-1]):
            for y in row[i+1:]:
                if x % y == 0:
                    sum_ += x / y
                    found = True
                    break
                elif y % x == 0:
                    sum_ += y / x
                    found = True
                    break
            if found:
                break
    return int(sum_)


def test2():
    spreadsheet = """5 9 2 8
                    9 4 7 3
                    3 8 6 5"""
    assert 9 == dividers_sum(parse(spreadsheet))


def part2():
    print(dividers_sum(parse(read())))


if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()