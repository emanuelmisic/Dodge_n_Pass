import pygame as pg
from sys import exit
from level import Level

from settings import *

BG = pg.image.load(os.path.join('assets', 'background_1.png'))

class Game:
    def __init__(self):
        # GENERAL SETUP
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game")
        self.clock = pg.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                    
            self.screen.blit(BG, (0,0))
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)
                    
if __name__ == '__main__':
	game = Game()
	game.run()
