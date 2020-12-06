#!/bin/env python3

def main():
    with open("input.txt") as fd:
        people_questions_by_group = [[set(questions) for questions in group.split("\n") if questions != ""] for group in fd.read().split("\n\n")]

    print("Part One = ", sum(map(lambda g: len(set.union(*g)), people_questions_by_group)))
    print("Part Two = ", sum(map(lambda g: len(set.intersection(*g)), people_questions_by_group)))


if __name__ == "__main__":
    main()
