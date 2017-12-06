"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

"""

import re


def read():
    with open('inputs/day4.txt') as fd:
        return [line.strip() for line in fd]


repeated_word_regex = re.compile(r'(\b\w+?\b).+(\b\1\b)')


def contains_repeated(passphrase):
    match = repeated_word_regex.search(passphrase)
    return True if match else False


def test1():
    assert not contains_repeated("aa bb cc dd ee")
    assert contains_repeated("aa bb cc dd aa")
    assert not contains_repeated("aa bb cc dd aaa")


def count_valid(passphrases):
    counter = 0
    for passphrase in passphrases:
        if not contains_repeated(passphrase):
            counter += 1
    return counter


def part1():
    print(count_valid(read()))


def contains_anagrams(passphrase):
    letter_sets = []
    for word in passphrase.split():
        w_set = sorted(word)
        if w_set in letter_sets:
            return True
        else:
            letter_sets.append(w_set)
    return False


def test2():
    assert not contains_anagrams('abcde fghij')
    assert contains_anagrams('abcde xyz ecdab')
    assert not contains_anagrams('a ab abc abd abf abj')
    assert not contains_anagrams('iiii oiii ooii oooi oooo')
    assert contains_anagrams('oiii ioii iioi iiio')


def count_valid2(passphrases):
    counter = 0
    for passphrase in passphrases:
        if not contains_anagrams(passphrase):
            counter += 1
    return counter


def part2():
    print(count_valid2(read()))

if __name__ == '__main__':
    # test1()
    # part1()
    # test2()
    part2()