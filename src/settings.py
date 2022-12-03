import os
import pygame

screen = pygame.display.set_mode((864, 864))

white = (255, 255, 255)
black = (0, 0, 0)

# Menu Variables
center_x = screen.get_width() / 2
center_y = screen.get_height() / 2
fill_x = 300
fill_y = 150
play_btn_pos = (center_x - fill_x / 2, center_y - fill_y / 2, fill_x, fill_y)

BG1 = pygame.image.load(os.path.join('assets', 'background_1.png'))

HEIGHT = 864
WIDTH = 864
FPS = 60
TILE_SIZE = 48
