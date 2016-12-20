from functools import partial

import pytest

from two_steps_forward import Floor

def test0():
    floor = Floor('ihgpwlah')
    assert floor.shortest_path() == 'DDRRRD'

def test1():
    floor = Floor('kglvqrro')
    assert floor.shortest_path() == 'DDUDRLRRUDRD'

def test2():
    floor = Floor('ulqzkmiv')
    assert floor.shortest_path() == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def test3():
    floor = Floor('ihgpwlah')
    assert floor.longest_path_non_recursive() == 370

def test4():
    floor = Floor('kglvqrro')
    assert floor.longest_path_non_recursive() == 492

def test5():
    floor = Floor('ulqzkmiv')
    assert floor.longest_path_non_recursive() == 830

if __name__ == "__main__":
    pytest.main(__file__)

