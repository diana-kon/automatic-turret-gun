class Color:
    r: int
    g: int
    b: int

    def __init__(self, r: int, g: int, b: int):
        self.r = self.__validate(r)
        self.g = self.__validate(g)
        self.b = self.__validate(b)

    # ensure the value is between 0 and 255
    def __validate(self, value: int) -> int:
        return value if 0 <= value <= 255 else (0 if value < 0 else 255)

    # this allows to compare two colors by value
    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    # this is needed for pretty and useful output in test results
    def __repr__(self):
        return f"Color({self.r} {self.g} {self.b})"
