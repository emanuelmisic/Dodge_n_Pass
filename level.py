import pygame as pg
from settings import *

from player import Player
from border import Border


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pg.display.get_surface()

        # sprite group setup
        self.visible_sprites = pg.sprite.Group()
        self.obstacle_sprites = pg.sprite.Group()
        
        self.create_map()
  
    def create_map(self):
        for row_index,row in enumerate(LEVEL1_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Border((x,y),[self.visible_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                    
    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        