
from typing import Any
import pygame
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
        ground_surf = pygame.image.load("assets/sprites/ground.png").convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * sclae_factor)

        # position
        self.rect = self.image.get_rect(bottomleft = (0, HEIGHT))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):   
        self.position.x -= 300 * dt
        if self.rect.centerx <= 0:
            self.position.x = 0

        self.rect.x = round(self.position.x)


class Plane(pygame.sprite.Sprite):
    def __init__(self, groups, sclae_factor):
        super().__init__(groups)

        self.import_frames(sclae_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        #rect
        self.rect =self.image.get_rect(midleft =(WIDTH / 20, HEIGHT / 2))
        self.position = pygame.math.Vector2(self.rect.toplesft)
    
        # movment
        self.gtavity = 20
        self.direction = 0
    
    def import_frames(self, scale_factor):
        self.frames = []
        for i in range(3):
            surf = pygame.image.load(f"assets/sprites/redbird{i}.png").convert_alpha()
            scale_surface = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scale_surface)

    def gravity(self, dt):
        self.direction +

    def update(self, dt):
        self.gravity(dt)