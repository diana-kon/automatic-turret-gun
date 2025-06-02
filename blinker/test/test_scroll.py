import blinker


def test_empty_changes_nothing():
    assert blinker.scroll([]) == []


def test_single_item_also_changes_nothing():
    assert blinker.scroll([blinker.RED]) == [blinker.RED]


def test_two_item_scroll_in_effect_reverses_items():
    assert blinker.scroll([blinker.RED, blinker.GREEN]) == [blinker.GREEN, blinker.RED]


def test_three_items_scroll():
    initial_lights = [blinker.RED, blinker.GREEN, blinker.PURPLE]
    expected_result = [blinker.GREEN, blinker.PURPLE, blinker.RED]
    actual_result = blinker.scroll(initial_lights)
    assert actual_result == expected_result


def test_full_eight_digit_scroll():
    lights = [
        blinker.PURPLE,
        blinker.GREEN,
        blinker.RED,
        blinker.BLACK,
        blinker.RED,
        blinker.GREEN,
        blinker.PURPLE,
        blinker.BLACK
    ]

    expected_result = [
        blinker.GREEN,
        blinker.RED,
        blinker.BLACK,
        blinker.RED,
        blinker.GREEN,
        blinker.PURPLE,
        blinker.BLACK,
        blinker.PURPLE
    ]

    updated_lights = blinker.scroll(lights)
    assert updated_lights == expected_result
