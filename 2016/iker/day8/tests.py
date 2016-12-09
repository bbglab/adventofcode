import pytest

from two_factor_auth import Screen

def test0():
    instructions = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4',
                    'rotate column x=1 by 1']
    screen = Screen(3,7)
    assert screen.apply_instructions(instructions) == 6


if __name__ == "__main__":
    pytest.main(__file__)

