import pygame as pgm
from entites.enemy import Type_A, Type_a
from settings import *

from entites.player import Player
from entites.border import Border
from exit import Exit


class Level:
    def __init__(self, level):

        self.level = level-1

        # get the display surface
        self.display_surface = pgm.display.get_surface()

        # sprite group setup
        self.visible_sprites = pgm.sprite.Group()
        self.obstacle_sprites = pgm.sprite.Group()
        self.benevolent_sprites = pgm.sprite.Group()
        self.bad_sprites = pgm.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(LEVEL_MAP[self.level]):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Border((x, y), [self.visible_sprites,
                           self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [
                                         self.visible_sprites], self.obstacle_sprites, self.benevolent_sprites, self.bad_sprites)
                if col == 'e':
                    Exit((x-24, y), [self.visible_sprites,
                         self.benevolent_sprites])
                if col == 'a':
                    Type_a((x, y), [self.visible_sprites,
                           self.bad_sprites], self.obstacle_sprites)
                if col == 'A':
                    Type_A((x, y), [self.visible_sprites,
                           self.bad_sprites], self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
