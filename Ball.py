from typing import Tuple


class Ball:
    def __init__(self, x: int, y: int, color: Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y
        self.color = color

    def move(self, d_x: int, d_y: int) -> None:
        self.x += d_x
        self.y += d_y

    def pos(self):
        return self.x, self.y
