import pygame
from sys import exit
from components.level import Level
from components.button import Button
from entites.player import Player

from settings import *

pygame.init()
pygame.display.set_caption("Dodge 'n Pass")
clock = pygame.time.Clock()

# load button images
start_img = pygame.image.load('assets\start_game_btn.png').convert_alpha()
quit_img = pygame.image.load('assets/quit_btn.png').convert_alpha()

# create button instances
# start
start_button = Button(0, 0, start_img)
start_button_width = start_button.get_width()
start_button_height = start_button.get_height()
start_button_draw = Button((WIDTH / 2) - (start_button_width / 2), (HEIGHT / 4) - (start_button_height / 2), start_img)
# quit
quit_button = Button(0, 0, quit_img)
quit_button_width = quit_button.get_width()
quit_button_height = quit_button.get_height()
quit_button_draw = Button((WIDTH / 2) - (quit_button_width / 2), (HEIGHT / 2) - (quit_button_height / 2), quit_img)

class Game:
    def __init__(self, level_num):
        self.level_num = level_num
        self.level = Level(level_num)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.blit(BG1, (0, 0))
            self.level.run()
            pygame.display.update()
            clock.tick(FPS)

class Menu:
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill((0, 0, 0))
            
            if start_button_draw.draw(screen):
                game = Game(1)
                game.run()
            
            if quit_button_draw.draw(screen):
                pygame.quit()
                exit()
            
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    menu = Menu()
    menu.run()
