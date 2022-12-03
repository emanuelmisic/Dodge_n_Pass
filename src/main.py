import pygame
from sys import exit
from level import Level

from settings import *

pygame.init()
pygame.display.set_caption("Dodge 'n Pass")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 64)

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
                #     game = Game(1)
                #     game.run()

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, white, (play_btn_pos))
            text = font.render("Play", True, black)
            textpos = text.get_rect(x=center_x, y=center_y)
            screen.blit(text, textpos)
            pygame.display.update()
            clock.tick(FPS)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
