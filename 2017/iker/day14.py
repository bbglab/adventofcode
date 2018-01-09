"""
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:

11.2.3..-->
.1.2.3.4
....5.6.
7.8.55.9
.88.5...
88..5..8
.8...8..
88.8.88.-->
|      |
V      V

Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?

"""

input = 'jxqlasbh'


# From day 10
import functools
import operator


def knot_hash(items, lengths):
    pos = 0
    for index, length in enumerate(lengths):
        if pos + length > len(items):
            size_1 = len(items[pos:])
            size_2 = length - size_1
            tmp = list(reversed(items[pos:] + items[:size_2]))
            items[pos:] = tmp[:size_1]
            items[:size_2] = tmp[size_1:]
        else:
            items[pos:pos+length] = list(reversed(items[pos:pos+length]))
        pos += index + length
        if pos >= len(items):
            pos = pos % len(items)
    return items


def knot_hash2(items, lengths):
    lengths = [ord(l) for l in lengths] + [17, 31, 73, 47, 23]
    sparse_hash = knot_hash(items, lengths*64)
    dense_hash = [functools.reduce(operator.xor, sparse_hash[16*v:16*(v+1)]) for v in range(16)]
    return ''.join(list(map('{:02x}'.format, dense_hash)))


def disk_hashes(key, size):
    for i in range(size):
        yield knot_hash2(list(range(256)), key+'-'+str(i))


def count_used(key, size):
    counter = 0
    for hash in disk_hashes(key, size):
        for v in hash:
            s01 = '{:04b}'.format(int(v, 16))
            counter += s01.count('1')
    return counter


def test1():
    assert 8108 == count_used('flqrgnkx', 128)


def part1():
    print(count_used(input, 128))


class Disk:

    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def _next(self):
        while True:
            for i, r in enumerate(self.matrix):
                if '1' in r:
                    yield i, r.index('1')
                    break
            else:
                raise StopIteration

    def _clean_adjancents(self, i, j):
        self.matrix[i] = self.matrix[i][:j] + '0' + self.matrix[i][j+1:]
        if i-1 >= 0 and self.matrix[i-1][j] == '1':
            self._clean_adjancents(i-1, j)
        if i+1 < self.size and self.matrix[i+1][j] == '1':
            self._clean_adjancents(i+1, j)
        if j-1 >= 0 and self.matrix[i][j-1] == '1':
            self._clean_adjancents(i, j-1)
        if j+1 < self.size and self.matrix[i][j+1] == '1':
            self._clean_adjancents(i, j+1)

    def count_regions(self):
        counter = 0
        for i, j in self._next():
            self._clean_adjancents(i, j)
            counter += 1
        return counter

def regions(key, size):
    f = functools.partial(int, base=16)
    disk = Disk([''.join(map('{:04b}'.format, map(f, hash))) for hash in disk_hashes(key, size)])
    return disk.count_regions()


def test2():
    assert 1242 == regions('flqrgnkx', 128)


def part2():
    print(regions(input, 128))


if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()
