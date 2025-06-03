import blinker


def test_empty_changes_nothing():
    assert blinker.scroll([]) == []


def test_single_item_also_changes_nothing():
    assert blinker.scroll([blinker.RED]) == [blinker.RED]


def test_two_item_scroll_in_effect_reverses_items():
    lights = [blinker.RED, blinker.GREEN]
    assert blinker.scroll(lights) == [blinker.GREEN, blinker.RED]


def test_three_items_scroll():
    initial_lights = [
        blinker.Color(1, 1, 1),
        blinker.Color(2, 2, 2),
        blinker.Color(3, 3, 3),
    ]
    expected_result = [
        blinker.Color(3, 3, 3),
        blinker.Color(1, 1, 1),
        blinker.Color(2, 2, 2),
    ]
    actual_result = blinker.scroll(initial_lights)
    assert actual_result == expected_result


def test_full_eight_digit_scroll():
    lights = [
        blinker.Color(1, 1, 1),
        blinker.Color(2, 2, 2),
        blinker.Color(3, 3, 3),
        blinker.Color(4, 4, 4),
        blinker.Color(5, 5, 5),
        blinker.Color(6, 6, 6),
        blinker.Color(7, 7, 7),
        blinker.Color(8, 8, 8),
    ]

    expected_result = [
        blinker.Color(8, 8, 8),
        blinker.Color(1, 1, 1),
        blinker.Color(2, 2, 2),
        blinker.Color(3, 3, 3),
        blinker.Color(4, 4, 4),
        blinker.Color(5, 5, 5),
        blinker.Color(6, 6, 6),
        blinker.Color(7, 7, 7),
    ]

    updated_lights = blinker.scroll(lights)
    assert updated_lights == expected_result
