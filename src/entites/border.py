import pygame
from settings import *


class Border(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('assets', 'border_x.png'))
        self.rect = self.image.get_rect(topleft=pos)
