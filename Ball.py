from typing import Tuple


class Ball:
    def __init__(self, x: int, y: int, color: Tuple[int, int, int, int]):
        self.x = x
        self.y = y
        self.color = color
