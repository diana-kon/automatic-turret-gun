RED = {"r": 255, "g": 0, "b": 0}
BLACK = {"r": 0, "g": 0, "b": 0}
PURPLE = {"r": 156, "g": 2, "b": 163}
GREEN = {"r": 0, "g": 255, "b": 0}

def slide(lights):
    updated_lights = []
    for i, l in enumerate(lights):
        if i > 0:
            updated_lights.append(l)
    updated_lights.append(BLACK)
    return updated_lights