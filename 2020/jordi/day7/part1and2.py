#!/bin/env python3

def count_shiny_gold(bags, key, visited):
    if key == "shiny gold":
        return 1
    if key in visited:
        return 0
    return sum(count_shiny_gold(bags, k, visited + [key]) for k in bags[key].keys())


def count_embedded_bags(bags, key, visited):
    return sum(v * (count_embedded_bags(bags, k, visited + [key]) + 1) for k, v in filter(lambda v: v[0] not in visited, bags[key].items()))


def main():
    # Parse input
    bags = {}
    with open("input.txt") as fd:
        for line in fd.readlines():
            bag, contains = line.strip().split(" bags contain ", 2)
            bags[bag] = dict((v[1], int(v[0])) for v in filter(lambda v: v[0] != "no", [i.strip().split(" ", 1) for i in contains.replace("bags", "").replace("bag", "").replace(".", "").split(",")]))

    # Count total bags with at least one shiny gold bag inside
    part1 = sum(count_shiny_gold(bags, k, []) > 0 for k in filter(lambda v: v != "shiny gold", bags.keys()))
    print("Part One:", part1)

    # Count total of bags inside the shiny gold bag
    part2 = count_embedded_bags(bags, "shiny gold", [])
    print("Part Two:", part2)


main()
