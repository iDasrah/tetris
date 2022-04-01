import pygame

import CONSTANTES
from CONSTANTES import *
from random import randint

from Grille import Grille
from pieces.Red import *
from pieces.Green import *


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.running = True
        self.current_piece = None
        self.grille = Grille()
        self.generate_piece()

    def run(self):
        while self.running:
            self.draw()
            self.update()
            self.events()

    def generate_piece(self):
        self.current_piece = PIECES[randint(0, len(PIECES) - 1)](CONSTANTES.SCREEN_WIDTH // 2, CONSTANTES.PIXEL_SIZE, self.surface)

    def draw(self):
        pygame.draw.rect(self.surface, pygame.Color(255, 247, 248),
                         pygame.Rect(0, 0, CONSTANTES.SCREEN_WIDTH, CONSTANTES.SCREEN_HEIGHT))
        self.grille.draw(self.surface)
        self.current_piece.draw()

    def update(self):
        self.current_piece.update()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.current_piece.next_config(1)
                if event.key == pygame.K_LEFT:
                    self.current_piece.next_config(-1)
                if event.key == pygame.K_q:
                    self.current_piece.move_piece('left')
                if event.key == pygame.K_d:
                    self.current_piece.move_piece('right')
                if event.key == pygame.K_s:
                    self.current_piece.move_piece('down')

