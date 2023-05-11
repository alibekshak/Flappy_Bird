# import pygame

# pygame.init()
# # Окно игры: размер, позиция
# gameScreen = pygame.display.set_mode((400, 300))
# # Модуль os - позиция окна
# import os
# x = 100
# y = 100
# os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
# # Параметры окна
# size = [500, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Test drawings")
# gameScreen.fill((0,0,255))
# pygame.display.flip()

from pygame.locals import *
import pygame
import sys
import time
from sprites import Background, Ground, Plane
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
        Ground(self.all_sprites, self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor)
        
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
                    

            pygame.display.update()
            # logic of game
            self.display_face.fill('black')
            self.all_sprites.update(dt)
            
            self.all_sprites.draw(self.display_face)

            self.clock.tick(FPS)

if __name__ == '__main__':
    game = FlappyBird()
    game.run()