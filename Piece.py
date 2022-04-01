import time

import pygame.draw
import CONSTANTES
from pygame import Color, Rect


class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, configs, color, surface, sizes):
        super().__init__()
        self.configs = configs
        self.config = 0
        self.color = color
        self.surface = surface
        self.sizes = sizes
        self.current_size = 0
        self.speed = CONSTANTES.PIXEL_SIZE
        self.rect = pygame.Rect(x, y, width * CONSTANTES.PIXEL_SIZE,
                                height * CONSTANTES.PIXEL_SIZE)
        self.now = time.time()

    def update(self):
        if time.time() - self.now >= 1:
            self.go_down()
            self.now = time.time()

    def draw(self):
        for coords in self.configs[self.config]:
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.rect.x + coords[1] * CONSTANTES.PIXEL_SIZE,
                                                                   self.rect.y + coords[0] * CONSTANTES.PIXEL_SIZE,
                                                                   CONSTANTES.PIXEL_SIZE, CONSTANTES.PIXEL_SIZE))
        self.draw_origin()

    def next_config(self, _next):
        if 0 <= self.config + _next <= 3 and 0 <= self.current_size + _next <= 3:
            self.config += _next
            self.current_size += _next
            self.rect.width = self.sizes[self.current_size][0] * CONSTANTES.PIXEL_SIZE
            self.rect.height = self.sizes[self.current_size][1] * CONSTANTES.PIXEL_SIZE
        else:
            self.config = 0
            self.current_size = 0
            self.rect.width = self.sizes[0][0] * CONSTANTES.PIXEL_SIZE
            self.rect.height = self.sizes[1][0] * CONSTANTES.PIXEL_SIZE

    def move_piece(self, direction):
        print(self.rect.y, self.rect.height, self.speed)
        if -1 < self.rect.x - self.speed and direction == 'left':
            self.rect.x -= self.speed
        if self.rect.x + self.rect.width + self.speed < CONSTANTES.SCREEN_WIDTH + 1 and direction == 'right':
            self.rect.x += self.speed
        if self.rect.y + self.rect.height + self.speed < CONSTANTES.SCREEN_HEIGHT + 1 and direction == 'down':
            self.rect.y += self.speed

    def go_down(self):
        if self.rect.y + self.rect.height + self.speed < CONSTANTES.SCREEN_HEIGHT + 1:
            self.rect.y += self.speed

    def draw_box(self):
        pygame.draw.rect(self.surface, pygame.color.Color(0, 0, 0),
                         pygame.rect.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height))

    def draw_origin(self):
        pygame.draw.rect(self.surface, pygame.color.Color(0, 0, 0), pygame.rect.Rect(self.rect.x, self.rect.y, 5, 5))
