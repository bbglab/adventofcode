import pytest

from radioisotope_thermoelectric_generators import Building

def test0():
    instructions = ['The first floor contains a hydrogen-compatible '
                    'microchip and a lithium-compatible microchip.',
                    'The second floor contains a hydrogen generator.',
                    'The third floor contains a lithium generator.',
                    'The fourth floor contains nothing relevant.']

    building = Building(instructions)
    assert building.solve() == 11

if __name__ == "__main__":
    pytest.main(__file__)

