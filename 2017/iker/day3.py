"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 361527.


--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...


"""
import math

# def get_ring(point):
#     numbers = 1
#     ring = 0  # get the ring in which the number is
#     while True:
#         ring += 1
#         numbers_in_ring = 4 * (ring*2 + 1)
#         numbers += numbers_in_ring
#         if point <= numbers:
#             break
#     return ring

def get_side(point):
    side = math.ceil(math.sqrt(point))
    if side % 2 == 0:
        side += 1
    return side

# def get_cardinals(ring):
#     right = 4 * ((ring-1)*2 + 1) + ring * 2
#     return right, right + (ring*2 + 1),  right + 2*(ring*2 + 1),  right + 3*(ring*2 + 1)
#


def get_displacement(point, ring):
    distances = []
    for i in [1,3,5,7]:
        distances.append(abs(point-i*ring))
    return min(distances)


def distance(point):
    if point == 1:
        return 0
    else:
        side = get_side(point)
        ring = (side - 1) // 2
        rescaled = point - (side-2)**2
        displacement = get_displacement(rescaled, ring)
        return displacement + ring


def test1():
    assert 0 == distance(1)
    assert 3 == distance(12)
    assert 2 == distance(23)
    assert 31 == distance(1024)


def part1():
    print(distance(361527))


if __name__ == '__main__':
    # test1()
    part1()