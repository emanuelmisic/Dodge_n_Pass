import pygame as pg
from settings import *

class Border(pg.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pg.image.load(os.path.join('assets', 'border_x.png'))
		self.rect = self.image.get_rect(topleft = pos)

	def get_rectvalue(self):
		return self.rect