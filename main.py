import pygame
from Game import *
from CONSTANTES import *

pygame.init()

size = SCREEN_WIDTH, SCREEN_HEIGHT

win = pygame.display.set_mode(size)

game = Game(win)
game.run()
