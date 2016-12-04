import pytest

from squares_with_three_sides import valid_triangles

def test0():
    triangles = [[5,10,25]]
    assert valid_triangles(triangles) == 0



if __name__ == "__main__":
    pytest.main(__file__)

