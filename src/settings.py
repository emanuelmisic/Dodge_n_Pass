import os
import pygame

from enum import Enum

screen = pygame.display.set_mode((864, 864))

white = (255, 255, 255)
black = (0, 0, 0)

BG1 = pygame.image.load(os.path.join('assets', 'background_1.png'))

HEIGHT = 864
WIDTH = 864
FPS = 60
TILE_SIZE = 48

class GameState(Enum):
    START = 'START'
    MENU = 'MENU'
    PAUSE = 'PAUSE'
    STOP = 'STOP'
