import pygame as pg
from pygame.math import Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.angle = 0

    def update(self, dt):
        self.velocity *= 0.99  # Apply friction
        self.position += self.velocity * dt
        self.rect.center = self.position

    def rotate_left(self):
        self.angle += 5

    def rotate_right(self):
        self.angle -= 5

    def accelerate(self):
        acceleration = Vector2(0, -0.1).rotate(-self.angle)
        self.velocity += acceleration
