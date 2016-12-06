import pytest

from signals_and_noise import get_message, get_message2

def test0():
    message = 'eedadn drvtee eandsr raavrd atevrs tsrnev sdttsa rasrtv ' \
              'nssdts ntnada svetve tesnvt vntsnd vrdear dvrsen ' \
              'enarar'.split(' ')
    assert get_message(message) == 'easter'

def test1():
    message = 'eedadn drvtee eandsr raavrd atevrs tsrnev sdttsa rasrtv ' \
              'nssdts ntnada svetve tesnvt vntsnd vrdear dvrsen ' \
              'enarar'.split(' ')
    assert get_message2(message) == 'advent'

if __name__ == "__main__":
    pytest.main(__file__)

