import os
import pygame

screen = pygame.display.set_mode((864, 864))

white = (255, 255, 255)
black = (0, 0, 0)

BG1 = pygame.image.load(os.path.join('assets', 'background_1.png'))

HEIGHT = 864
WIDTH = 864
FPS = 60
TILE_SIZE = 48

GAME_STATE_START = 'START'
GAME_STATE_MENU = 'MENU'
