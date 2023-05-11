from pygame.locals import *
import pygame
import sys
import time
from sprites import Background, Ground, Plane, Obstacle
from settings import *


class FlappyBird:
    def __init__(self):
        pygame.init()
        self.display_face = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game Flappy Bird")
        self.clock = pygame.time.Clock()

        # sprites_groups
        self.all_sprites = pygame.sprite.Group() 
        self.collision_sprites = pygame.sprite.Group() 

        #scale 
        bg_height = pygame.image.load("assets/sprites/background-night.png").get_height()
        self.scale_factor = HEIGHT / bg_height
        
        # setup sprite
        Background(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor)
        
        #time
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer,1400)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False):
            pygame.quit()
            sys.exit()


    def run(self):
        last_time = time.time()
        while True:

            #delta time(разница между текущим и предыдущим кадром)
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # команда для  использования  пробела
                    if event.key == pygame.K_SPACE:
                            self.plane.jump()
                elif event.type == pygame.MOUSEBUTTONDOWN: # команда для  использования мышки
                    self.plane.jump()
                
                if event.type == self.obstacle_timer:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor)

            pygame.display.update() 
            # logic of game
            self.display_face.fill('black')
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_face)

            self.clock.tick(FPS)

if __name__ == '__main__':
    game = FlappyBird()
    game.run()