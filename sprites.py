from typing import Any
import pygame
from pygame.sprite import _Group
from settings import *

class Background(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load("assets/sprites/back_g.jpeg").convert()

        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        full_size = pygame.transform.scale(bg_image, (full_width, full_height))

        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_size,(0,0))
        self.image.blit(full_size,(full_width,0))

        self.rect = self.image.get_rect(topleft = (0, 0))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.position.x -= 300 * dt
        if self.rect.right <= 0:
            self.position.x = 0
        self.rect.x = round(self.position.x)


class Ground(pygame.sprite.Sprite):
    def __init__(self, groups, sclae_factor):
        super().__init__(groups)
        ground_surf = pygame.image.load("").convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * sclae_factor)

        # position
        self.rect = self.image.get_rect(bottomleft = (0, HEIGHT))