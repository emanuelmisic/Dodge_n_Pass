import pygame
from settings import *


class Exit(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('assets', 'exit_e.png'))
        self.rect = self.image.get_rect(topleft=pos)
