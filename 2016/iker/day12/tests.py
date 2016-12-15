import pytest

from leonardo_s_monorail import Computer

def test0():
    program = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']

    computer = Computer()
    computer.run(program)
    assert computer.get('a') == 42

if __name__ == "__main__":
    pytest.main(__file__)

