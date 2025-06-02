from .color import Color


RED = Color(255, 0, 0)
BLACK = Color(0, 0, 0)
PURPLE = Color(156, 2, 163)
GREEN = Color(0, 255, 0)


def slide(lights: list[Color]) -> list[Color]:
    updated_lights = list()
    for i, light in enumerate(lights):
        if i > 0:
            updated_lights.append(light)
    updated_lights.append(BLACK)
    return updated_lights


def scroll(lights):
    return None
