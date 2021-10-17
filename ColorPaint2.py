import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")

keep_going = True
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
radius = 8
mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        if pygame.key.get_pressed()[pygame.K_r]:
            button_color = RED
        elif pygame.key.get_pressed()[pygame.K_b]:
            button_color = BLUE
        else:
            button_color = YELLOW
    if mousedown:
            spot = pygame.mouse.get_pos()
            pygame.draw.circle(screen, button_color, spot, radius)
    pygame.display.update()

pygame.quit()
