import os


def valid_triangles(triangles):
    valid = 0
    for dimensions in triangles:
        longest = max(dimensions)
        rest = sum(dimensions) - longest
        if rest > longest:
            valid += 1
    return valid

def make_groups(triangles):
    output = []
    traspose = [list(i) for i in zip(*triangles)]
    for row in traspose:
        output+=([row[i:i+3] for i in range(0, len(row), 3)])
    return output

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    triangles = []
    with open(file) as fd:
        for line in fd:
            triangles.append(list(map(int, line.strip().split())))
    print('Part1: ', valid_triangles(triangles))

    print('Part 2:', valid_triangles(make_groups(triangles)))
