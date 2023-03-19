# Start the game have options for pinball, pinball with set start and then a fractal explorer
import pygame, sys
pygame.init()

from settings import *

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.function = function
        self.colour = BLUE
        
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    def func(self):
        self.function()
        return self.function()
    
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.func()
            print(self.func())

    def select(self):
        self.func()
    
    def is_selected(self):
        self.colour = RED
    
    def not_selected(self):
        self.colour = BLUE

def pinball():
    print("interaction")

def main():

    buttons = []
    buttons.append(Button(screenWidth* 1/4, 250, 100, 50, pinball))
    buttons.append(Button(screenWidth* 2/4, 250, 100, 50, pinball))
    buttons.append(Button(screenWidth* 3/4, 250, 100, 50, pinball))
    buttons[0].is_selected()
    selection = 0
    menu = True
    while menu:
        # set clock
        clock.tick(30)

        #event loop
        for event in pygame.event.get():
            # bomb out of loop if quit
            if event.type == pygame.QUIT:
                menu = False
            
        if pygame.mouse.get_pressed():
            for b in buttons:
                b.check_click(pygame.mouse.get_pos())
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            selection = (selection - 1) % len(buttons)
        if keys[pygame.K_RIGHT]:
            selection = (selection + 1) % len(buttons)
        if keys[pygame.K_SPACE]:
            buttons[selection].select()

        for i in buttons:
            if i == buttons[selection]:
                i.is_selected()
            else:
                i.not_selected()

        win.fill(BLACK)
        for i in buttons:
            i.draw(win)
        # win.blit(pygame.image.load('bcg.img'), (screenWidth/2 - 225, 100))
        win.blit(myfont.render('Choose option', True, WHITE), (screenWidth/2 - 220, 100))
        win.blit(smallfont.render('Pinball', True, WHITE), (screenWidth* 1/4, 250))
        win.blit(smallfont.render('Map', True, WHITE), (screenWidth* 2/4, 250))
        win.blit(smallfont.render('fractal', True, WHITE), (screenWidth* 3/4, 250))

        pygame.display.update()

main()