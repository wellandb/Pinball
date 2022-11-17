import pygame, random
from settings import *

def mouseClick():
    pygame.draw.circle(win,red,mouse,7)
    print(mouse)

run = True
while run:
    
    clock.tick(30)
    
    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick()
    

    pygame.display.update()

pygame.quit()