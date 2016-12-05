import pytest

from how_about_a_nice_game_of_chess import find_password, find_password2

def test0():
    id = "abc"
    assert find_password(id) == "18f47a30"

def test1():
    id = "abc"
    assert find_password2(id) == "05ace8e3"

if __name__ == "__main__":
    pytest.main(__file__)

