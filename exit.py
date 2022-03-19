import pygame as pg
from settings import *

class Exit(pg.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pg.image.load(os.path.join('assets', 'exit_e.png'))
		self.rect = self.image.get_rect(topleft = pos)