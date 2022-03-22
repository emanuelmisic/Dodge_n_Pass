import pygame as pg
from sys import exit
from level import Level

from settings import *

BG = pg.image.load(os.path.join('assets', 'background_1.png'))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Dodge 'n Pass")
clock = pg.time.Clock()

class Game:
    def __init__(self, level_n):
        
        self.level_n = level_n
        self.level = Level(level_n)
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                    
            screen.blit(BG, (0,0))
            self.level.run()
            pg.display.update()
            clock.tick(FPS)
                    
class Menu:
    def __init__(self):
        pass
    
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    game = Game(1)
                    game.run()

            screen.fill((0,0,0))
            pg.display.update()
            clock.tick(FPS)                


if __name__ == '__main__':
	menu = Menu()
	menu.run()
