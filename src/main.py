import pygame as pgm
from sys import exit
from level import Level

from settings import *

BG = pgm.image.load(os.path.join('assets', 'background_1.png'))

pgm.init()
screen = pgm.display.set_mode((WIDTH, HEIGHT))
pgm.display.set_caption("Dodge 'n Pass")
clock = pgm.time.Clock()


class Game:
    def __init__(self, level_num):

        self.level_num = level_num
        self.level = Level(level_num)

    def run(self):
        while True:
            for event in pgm.event.get():
                if event.type == pgm.QUIT:
                    pgm.quit()
                    exit()

            screen.blit(BG, (0, 0))
            self.level.run()
            pgm.display.update()
            clock.tick(FPS)


class Menu:
    def __init__(self):
        pass

    def run(self):
        while True:
            for event in pgm.event.get():
                if event.type == pgm.QUIT:
                    pgm.quit()
                    exit()
                if event.type == pgm.MOUSEBUTTONDOWN:
                    game = Game(1)
                    game.run()

            screen.fill((0, 0, 0))
            pgm.display.update()
            clock.tick(FPS)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
