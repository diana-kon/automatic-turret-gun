import blinker

def test_slide():

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
        blinker.BLACK
    ]

    updated_lights = blinker.slide(lights)
    assert updated_lights == expected_result

def test_scroll():

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