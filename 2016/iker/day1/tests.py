import pytest

from no_time_for_a_taxicab import move, get_first_revisit

def test0():
    instructions = 'R2, L3'.split(', ')
    assert move(instructions) == 5

def test1():
    instructions = 'R2, R2, R2'.split(', ')
    assert move(instructions) == 2

def test2():
    instructions = 'R5, L5, R5, R3'.split(', ')
    assert move(instructions) == 12

def test3():
    instructions = 'R8, R4, R4, R8'.split(', ')
    assert get_first_revisit(instructions) == 4


if __name__ == "__main__":
    pytest.main(__file__)
