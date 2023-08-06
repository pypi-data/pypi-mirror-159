from . import results


class Number:
    def __init__(self, value: int) -> None:
        self.value = value

    def compare(self, value: int):
        if self.value > value:
            return results.Greater
        if self.value < value:
            return results.Less
        if self.value == value:
            return results.Equal
