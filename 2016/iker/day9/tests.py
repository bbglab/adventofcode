import pytest

from explosives_in_cyberspace import decompress, count_letters, \
    decompress_v2, count_decompress, count_decompress_v2

def test0():
    string = 'ADVENT'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 6
    assert decompressed_string == 'ADVENT'

def test1():
    string = 'A(1x5)BC'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 7
    assert decompressed_string == 'ABBBBBC'

def test2():
    string = '(3x3)XYZ'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 9
    assert decompressed_string == 'XYZXYZXYZ'

def test3():
    string = 'A(2x2)BCD(2x2)EFG'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 11
    assert decompressed_string == 'ABCBCDEFEFG'

def test4():
    string = '(6x1)(1x3)A'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 6
    assert decompressed_string == '(1x3)A'

def test5():
    string = 'X(8x2)(3x3)ABCY'
    decompressed_string = decompress(string)
    assert count_letters(decompressed_string) == 18
    assert decompressed_string == 'X(3x3)ABC(3x3)ABCY'


def test6():
    string = '(3x3)XYZ'
    decompressed_string = decompress_v2(string)
    assert count_letters(decompressed_string) == 9
    assert decompressed_string == 'XYZXYZXYZ'

def test7():
    string = 'X(8x2)(3x3)ABCY'
    decompressed_string = decompress_v2(string)
    assert count_letters(decompressed_string) == len('XABCABCABCABCABCABCY')
    assert decompressed_string == 'XABCABCABCABCABCABCY'

def test8():
    string = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    decompressed_string = decompress_v2(string)
    assert count_letters(decompressed_string) == 241920
    assert decompressed_string == 'A'*241920

def test9():
    string = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    decompressed_string = decompress_v2(string)
    assert count_letters(decompressed_string) == 445

def test10():
    string = 'ADVENT'
    assert count_decompress(string) == 6

def test11():
    string = 'A(1x5)BC'
    assert count_decompress(string) == 7

def test12():
    string = '(3x3)XYZ'
    assert count_decompress(string) == 9

def test13():
    string = 'A(2x2)BCD(2x2)EFG'
    assert count_decompress(string) == 11

def test14():
    string = '(6x1)(1x3)A'
    assert count_decompress(string) == 6

def test15():
    string = 'X(8x2)(3x3)ABCY'
    assert count_decompress(string) == 18


def test16():
    string = '(3x3)XYZ'
    assert  count_decompress_v2(string) == 9

def test17():
    string = 'X(8x2)(3x3)ABCY'
    assert  count_decompress_v2(string) == len('XABCABCABCABCABCABCY')

def test18():
    string = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    assert  count_decompress_v2(string) == 241920

def test19():
    string = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    assert count_decompress_v2(string) == 445

if __name__ == "__main__":
    pytest.main(__file__)

