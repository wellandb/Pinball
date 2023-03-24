# Importing necessary modules
import pygame, random
from settings import *

# mouse click function to create a peg at the mouse location
def mouseClick():
    pygame.draw.circle(win,RED,mouse,7)

# loop to run window and board creation
run = True
while run:
    
    # frame rate
    clock.tick(30)
    
    # get position of the mouse
    mouse = pygame.mouse.get_pos()
    
    # event check
    for event in pygame.event.get():
        # if escape pressed then quit the window
        if event.type == pygame.QUIT:
            run = False
        # if mouse presssed then run mouse click function
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick()
    
    # display the updates on the screen
    pygame.display.update()
# quit pygame
pygame.quit()