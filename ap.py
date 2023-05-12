import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scoreboard")

font = pygame.font.Font(None, 36)

score = 0
high_score = 0

def update_score(new_score):
    global score, high_score
    score = new_score
    if score > high_score:
        high_score = score

def draw_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    high_score_text = font.render("High Score: " + str(high_score), True, WHITE)
    screen.blit(high_score_text, (10, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Update game logic here
    # ...

    # Render
    screen.fill(BLACK)
    draw_score()
    pygame.display.flip()