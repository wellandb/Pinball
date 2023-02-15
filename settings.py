#import pygame and random generator
import pygame, random, sys, math, numpy as np
# initialise pygame
pygame.init()

# intialise some colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (128, 128, 128)

#window
screenWidth = 1200
screenHeight = 600
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill(BLACK)

# text set up
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)
smallfont = pygame.font.SysFont('Arial', 20)

# setting a caption for game window
pygame.display.set_caption('Pinball')

# setting up clock
clock = pygame.time.Clock()