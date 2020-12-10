def get_position(data, x, y):
    if y >= len(data) or x <= 0 or y <= 0:
        raise ValueError("Outside the map")
    line = data[y]
    xm = x % len(line)
    return line[xm]


def main():
    with open("input.txt") as fd:
        data = [line.strip() for line in fd.readlines()]

    x, y = 0, 0
    trees = 0
    total_trees = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        try:
            while True:
                x += slope[0]
                y += slope[1]
                m = get_position(data, x, y)
                if m == "#":
                    trees += 1
        except ValueError:
            pass
        total_trees *= trees
        trees = 0
        x, y = 0, 0

    print(f"There is a {total_trees} trees product.")


main()
