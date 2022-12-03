import pygame as pgm
from settings import *


class Exit(pgm.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pgm.image.load(os.path.join('assets', 'exit_e.png'))
        self.rect = self.image.get_rect(topleft=pos)
