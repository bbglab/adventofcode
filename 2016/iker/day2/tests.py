import pytest

from bathroom_security import get_code, get_code2

def test0():
    instructions = 'ULL RRDDD LURDL UUUUD'.split(' ')
    assert get_code(instructions) == 1985


def test1():
    instructions = 'ULL RRDDD LURDL UUUUD'.split(' ')
    assert get_code2(instructions) == '5DB3'

if __name__ == "__main__":
    pytest.main(__file__)

