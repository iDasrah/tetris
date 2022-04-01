from Piece import *
from pygame import Color


class Red(Piece):
    def __init__(self, x, y, surface):
        self.surface = surface
        self.color = Color(209, 96, 61)
        self.configs = [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)],
                        [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, -1), (0, -2), (0, -3)]]
        self.sizes = [(1, 4), (4, 1), (1, 4), (4, 1)]

        super().__init__(x, y, self.sizes[0][0], self.sizes[1][0], self.configs, self.color, surface, self.sizes)
