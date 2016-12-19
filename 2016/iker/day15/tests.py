from functools import partial

import pytest

from timing_is_everything import Sculpture

def test0():
   design = ['Disc #1 has 5 positions; at time=0, it is at position 4.',
                'Disc #2 has 2 positions; at time=0, it is at position 1.']
   sculputre = Sculpture(design)

   assert sculputre.solve() == 5

if __name__ == "__main__":
    pytest.main(__file__)

