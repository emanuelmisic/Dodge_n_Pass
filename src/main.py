import pygame
from sys import exit
from components.level import Level

from settings import *
from components.button import Button

pygame.init()
pygame.display.set_caption("Dodge 'n Pass")
clock = pygame.time.Clock()

# load button images
start_img = pygame.image.load('assets\start_game_btn.png').convert_alpha()

# create button instances
# start
start_button = Button(0, 0, start_img)
start_button_width = start_button.get_width()
start_button_height = start_button.get_height()
start_button_draw = Button((WIDTH / 2) - (start_button_width / 2), (HEIGHT / 4) - (start_button_height / 2), start_img)

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
    def __init__(self):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pass
                    # game = Game(1)
                    # game.run()

            screen.fill((0, 0, 0))
            
            if start_button_draw.draw(screen):
                game = Game(1)
                game.run()
            
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    menu = Menu()
    menu.run()
