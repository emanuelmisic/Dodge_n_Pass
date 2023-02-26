import pygame
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)


class Type_a(Enemy):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(
            os.path.join('assets', 'enemy_type_a.png'))
        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites

        self.direction = pygame.math.Vector2(x=-1)
        self.speed = 2

    def move(self, speed):
        self.rect.x += self.direction.x * speed
        self.collision()

    def collision(self):
        for sprite in self.obstacle_sprites:
            if self.rect.colliderect(sprite.rect):
                if self.direction.x > 0:
                    self.direction.x = -1
                else:
                    self.direction.x = 1

    def update(self):
        self.move(self.speed)


class Type_A(Enemy):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(
            os.path.join('assets', 'enemy_type_a.png'))
        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites

        self.direction = pygame.math.Vector2(y=-1)
        self.speed = 2

    def move(self, speed):
        self.rect.y += self.direction.y * speed
        self.collision()

    def collision(self):
        for sprite in self.obstacle_sprites:
            if self.rect.colliderect(sprite.rect):
                if self.direction.y > 0:
                    self.direction.y = -1
                else:
                    self.direction.y = 1

    def update(self):
        self.move(self.speed)


class Type_b(Enemy):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(
            os.path.join('assets', 'enemy_type_b.png'))
        self.rect = self.image.get_rect(topleft=pos)

        self.obstacle_sprites = obstacle_sprites

        self.direction = pygame.math.Vector2(x=-1)
        self.speed = 4

    def move(self, speed):
        self.rect.x += self.direction.x * speed
        self.collision()

    def collision(self):
        for sprite in self.obstacle_sprites:
            if self.rect.colliderect(sprite.rect):
                if self.direction.x > 0:
                    self.direction.x = -1
                else:
                    self.direction.x = 1

    def update(self):
        self.move(self.speed)


class Type_B(Enemy):
    pass
