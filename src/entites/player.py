import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, benevolent_sprites, bad_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('assets', 'player.png'))
        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites
        self.benevolent_sprites = benevolent_sprites
        self.bad_sprites = bad_sprites

        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = 4.5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom
            for sprite in self.bad_sprites:
                if sprite.rect.colliderect(self.rect):
                    self.rect.topleft = self.pos

    def update(self):
        self.input()
        self.move(self.speed)
