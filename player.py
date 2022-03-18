import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load(os.path.join('assets', 'player.png'))
        self.rect = self.image.get_rect(topleft = pos)

        self.obstacle_sprites = obstacle_sprites
        
        self.vel = 4
        
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]: # left
            self.rect.x -= self.vel
        if keys[pg.K_RIGHT]: # right
            self.rect.x += self.vel
        if keys[pg.K_UP]: # up
            self.rect.y -= self.vel
        if keys[pg.K_DOWN]: # down
            self.rect.y += self.vel

    def update(self):
        self.move()
