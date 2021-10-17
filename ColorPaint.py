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
    if mousedown:
            spot = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                button_color = RED
            elif pygame.mouse.get_pressed()[1]:
                button_color = BLUE
            else:
                button_color = YELLOW
            pygame.draw.circle(screen, button_color, spot, radius)
    pygame.display.update()

pygame.quit()
