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
        self.active = True  # status of the game 

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

        #text
        self.font = pygame.font.Font("assets/sprites/BD_Cartoon_Shout.ttf", 30)
        self.score = 0
        self.start_off = 0

        # menu
        self.menu_surf = pygame.image.load("assets/sprites/message.png").convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center = (WIDTH / 2, HEIGHT / 2))

        # music
        self.music = pygame.mixer.Sound("assets/audio/Ghostrifter-Official-Subtle-Break.wav")
        self.music.play(loops= -1) # указываем что музыка будет повторятся бесконечно

        # save score
        self.high_scores = []
        self.load_high_scores()

    def load_high_scores(self):
        try:
            with open("leaderboard.txt", "r") as file:
                scores = file.readlines()
                self.high_scores = [int(score.strip()) for score in scores]
        except FileNotFoundError:
            self.high_scores = []

    def save_high_scores(self):
        with open("leaderboard.txt", "w") as file:
            for score in self.high_scores:
                file.write(str(score) + "\n")

    def update_high_scores(self):
        if self.score > 0:
            self.high_scores.append(self.score)
            self.high_scores.sort(reverse=True)
            self.high_scores = self.high_scores[:1]  # Keep only the top 1 scores
            self.save_high_scores()

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask)\
            or self.plane.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active = False
            self.plane.kill()

    def score_display(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_off) // 1000
            y = HEIGHT / 10
        else:
            y = HEIGHT / 2 + (self.menu_rect.height / 1.5) # будет отображать очки за игру ниже меню 

        score_surf = self.font.render(str(self.score), True, 'black')
        score_rect = score_surf.get_rect(midtop = (WIDTH / 2, y))
        self.display_face.blit(score_surf, score_rect)

        
    def draw_leaderboard(self):
        leaderboard_text = self.font.render("Top one", True, 'black')
        leaderboard_rect = leaderboard_text.get_rect(midtop=(WIDTH / 2, HEIGHT / 2 - 300))
        self.display_face.blit(leaderboard_text, leaderboard_rect)

        y = HEIGHT / 2 - 250
        for i, score in enumerate(self.high_scores):
            score_text = self.font.render(f"{i+1}. {score}", True, 'black')
            score_rect = score_text.get_rect(midtop=(WIDTH / 2, y))
            self.display_face.blit(score_text, score_rect)
            y += 250

    def run(self):
        last_time = time.time()
        while True:

            #delta time(разница между текущим и предыдущим кадром)
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # команда для  использования  пробела
                    if event.key == pygame.K_SPACE:
                            if self.active:
                                self.plane.jump()
                            else:
                                self.plane = Plane(self.all_sprites, self.scale_factor)
                                self.active = True
                                self.start_off = pygame.time.get_ticks()

                elif event.type == pygame.MOUSEBUTTONDOWN: # команда для  использования мышки
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor)
                        self.active = True
                
                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor)

            # logic of game
            self.display_face.fill('blue')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_face)
            self.score_display()

            if self.active:
                self.collisions()
            else:
                self.display_face.blit(self.menu_surf, self.menu_rect)
                self.update_high_scores()
                self.draw_leaderboard()

            pygame.display.update() 
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = FlappyBird()
    game.run()