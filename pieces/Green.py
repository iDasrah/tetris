from Piece import *
from pygame import Color


class Green(Piece):
    def __init__(self, x, y, surface):
        self.surface = surface
        self.color = Color(53, 176, 114)
        self.configs = [[(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (0, 1), (1, 1)],
                        [(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (0, 1), (1, 1)]]
        self.sizes = [(2, 2), (2, 2), (2, 2), (2, 2)]

        super().__init__(x, y, self.sizes[0][0], self.sizes[1][0], self.configs, self.color, surface, self.sizes)
