import pytest

from security_through_obscurity import sum_valid_sectors

def test0():
    rooms = ['aaaaa-bbb-z-y-x-123[abxyz]',
             'a-b-c-d-e-f-g-h-987[abcde]',
             'not-a-real-room-404[oarel]',
             'totally-real-room-200[decoy]']
    assert sum_valid_sectors(rooms) == 1514




if __name__ == "__main__":
    pytest.main(__file__)

