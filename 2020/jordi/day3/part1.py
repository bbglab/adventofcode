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
    try:
        while True:
            x += 3
            y += 1
            m = get_position(data, x, y)
            if m == "#":
                trees += 1
    except ValueError:
        pass

    print(f"There are {trees} trees.")


if __name__ == "__main__":
    main()
