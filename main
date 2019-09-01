import pygame
from random import randint

from Ball import Ball


pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling balls")

clock = pygame.time.Clock()
fps = 50

running = True
key_pressed = False

list_of_balls = []

# real velocity = fps * ball_velocity
ball_velocity = 2
ball_radius = 10

screen_buffer = pygame.Surface(screen.get_size())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            list_of_balls.append(Ball(x, y, (randint(0, 255), randint(0, 255), randint(0, 255))))

    screen_buffer.fill(pygame.Color("black"))
    for ball in list_of_balls:
        pygame.draw.circle(screen_buffer, ball.color, ball.pos(), ball_radius)
    screen.blit(screen_buffer, (0, 0))

    pygame.display.flip()

    for ball in list_of_balls:
        if ball.y <= height - ball_radius:
            ball.move(0, ball_velocity)

    clock.tick(fps)

pygame.quit()
