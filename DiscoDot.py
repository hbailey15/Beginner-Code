import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
GREEN = (255,0,255)       #RGB color triplet for GREEN
radius = 100


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(screen, color, (400,300), radius)
    pygame.display.update()

pygame.quit()
