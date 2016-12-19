from functools import partial

import pytest

from dragon_checksum import generate_data, get_checksum, fill_disk

def test_data_generation():
   assert generate_data('1') == '100'
   assert generate_data('0') == '001'
   assert generate_data('11111') == '11111000000'
   assert generate_data('111100001010') == '1111000010100101011110000'

def test_checksum():
    assert get_checksum('110010110100') == '100'

def test0():
    size = 20
    initial_state = '10000'
    _, checksum = fill_disk(size, initial_state)
    assert checksum == '01100'

if __name__ == "__main__":
    pytest.main(__file__)

