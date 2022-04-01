from Piece import *
from pygame import Color


class Yellow(Piece):
    def __init__(self, x, y, surface):
        self.surface = surface
        self.color = Color(247, 207, 27)
        self.configs = [[(0, 0), (0, -1), (1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1), (2, 0)],
                        [(0, 0), (0, -1), (1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1), (2, 0)]]
        self.sizes = [(3, 2), (2, 3), (3, 2), (2, 3)]

        super().__init__(x, y, self.sizes[0][0], self.sizes[1][0], self.configs, self.color, surface, self.sizes)
