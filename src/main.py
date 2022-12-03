import pygame
from sys import exit
from level import Level

from settings import *

BG = pygame.image.load(os.path.join('assets', 'background_1.png'))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge 'n Pass")
clock = pygame.time.Clock()


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

            screen.blit(BG, (0, 0))
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
            # pygame.draw.rect(screen, (255, 255, 255), )
            pygame.display.update()
            clock.tick(FPS)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
