import os
import pygame

from enum import Enum

BG1 = pygame.image.load(os.path.join('assets', 'background_1.png'))
BG2 = pygame.image.load(os.path.join('assets', 'background_2.png'))

HEIGHT = 864
WIDTH = 864
FPS = 60
TILE_SIZE = 48

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pause_bg = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pause_bg.fill((0, 0, 0, 80))

class GameState(Enum):
    START = 'START'
    MENU = 'MENU'
    PAUSE = 'PAUSE'
    STOP = 'STOP'
