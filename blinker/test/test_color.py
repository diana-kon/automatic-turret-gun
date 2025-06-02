import blinker


def test_it_accepts_values_within_range():
    color = blinker.Color(0, 128, 255)
    assert color.r == 0
    assert color.g == 128
    assert color.b == 255


def test_it_replaces_too_small_value_with_zero():
    color = blinker.Color(-1, 128, 255)
    assert color.r == 0
    assert color.g == 128
    assert color.b == 255


def test_it_replaces_too_large_value_with_white():
    color = blinker.Color(0, 128, 2000)
    assert color.r == 0
    assert color.g == 128
    assert color.b == 255
