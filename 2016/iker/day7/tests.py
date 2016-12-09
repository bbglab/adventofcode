import pytest

from internet_protocol_v7 import count_ips_with_tls, count_ips_with_ssl

def test0():
    ips = ['abba[mnop]qrst', 'abcd[bddb]xyyx', 'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn']
    assert count_ips_with_tls(ips) == 2

def test1():
    ips = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']
    assert count_ips_with_ssl(ips) == 3


if __name__ == "__main__":
    pytest.main(__file__)

