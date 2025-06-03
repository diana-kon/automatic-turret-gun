from .color import Color


RED = Color(255, 0, 0)
BLACK = Color(0, 0, 0)
PURPLE = Color(156, 2, 163)
GREEN = Color(0, 255, 0)
RED2 = Color(128, 0, 0)
BLACK2 = Color(0, 128, 0)
PURPLE2 = Color(156, 128, 163)
GREEN2 = Color(0, 128, 0)


def slide(lights: list[Color]) -> list[Color]:
    updated_lights = list()
    for i, light in enumerate(lights):
        if i > 0:
            updated_lights.append(light)
    updated_lights.append(BLACK)
    return updated_lights



##1st test pass
def scroll(lights: list[Color]) -> list[Color]:
    if len(lights) == 0:
        return lights
    last = lights[-1]
    new = [last] + lights
    new.pop()
    return new
