from functools import partial

import pytest

from one_time_pad import index_of_key, generate_keys

def test0():
    salt = "abc"
    keys_generator = partial(generate_keys, salt)
    assert index_of_key(keys_generator, 64) == 22728

if __name__ == "__main__":
    pytest.main(__file__)

