import pytest

from a_maze_of_twisty_little_cubicles import Maze

def test0():

    maze = Maze(10)

    assert maze.reach((7,4)) == 11


if __name__ == "__main__":
    pytest.main(__file__)

